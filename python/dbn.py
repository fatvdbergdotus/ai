import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# =====================
# RBM
# =====================
class RBM(nn.Module):
    def __init__(self, n_visible, n_hidden):
        super().__init__()
        self.W = nn.Parameter(torch.randn(n_visible, n_hidden) * 0.01)
        self.h_bias = nn.Parameter(torch.zeros(n_hidden))
        self.v_bias = nn.Parameter(torch.zeros(n_visible))

    def sample_h(self, v):
        prob_h = torch.sigmoid(v @ self.W + self.h_bias)
        return prob_h, torch.bernoulli(prob_h)

    def sample_v(self, h):
        prob_v = torch.sigmoid(h @ self.W.t() + self.v_bias)
        return prob_v, torch.bernoulli(prob_v)

    def contrastive_divergence(self, v, k=1, lr=0.01):
        v0 = v

        prob_h0, h0 = self.sample_h(v0)

        vk = v0
        for _ in range(k):
            _, hk = self.sample_h(vk)
            _, vk = self.sample_v(hk)

        prob_hk, _ = self.sample_h(vk)

        # Update
        self.W.data += lr * (v0.t() @ prob_h0 - vk.t() @ prob_hk) / v0.size(0)
        self.v_bias.data += lr * torch.mean(v0 - vk, dim=0)
        self.h_bias.data += lr * torch.mean(prob_h0 - prob_hk, dim=0)


# =====================
# DBN
# =====================
class DBN:
    def __init__(self, layer_sizes):
        self.rbms = []
        for i in range(len(layer_sizes) - 1):
            self.rbms.append(RBM(layer_sizes[i], layer_sizes[i+1]).to(device))

    def pretrain(self, dataloader, epochs=5, lr=0.01):
        input_data = None

        for i, rbm in enumerate(self.rbms):
            print(f"\nPretraining RBM {i+1}/{len(self.rbms)}")

            for epoch in range(epochs):
                total_loss = 0

                for images, _ in dataloader:
                    images = images.view(images.size(0), -1).to(device)

                    if input_data is not None:
                        images = input_data(images)

                    rbm.contrastive_divergence(images, lr=lr)

                print(f"Epoch {epoch+1} done")

            # Freeze this layer and define forward pass
            def transform(x, rbm=rbm):
                prob_h, _ = rbm.sample_h(x)
                return prob_h.detach()

            input_data = transform


# =====================
# Classifier
# =====================
class DBNClassifier(nn.Module):
    def __init__(self, dbn, num_classes=10):
        super().__init__()

        layers = []
        for rbm in dbn.rbms:
            linear = nn.Linear(rbm.W.size(0), rbm.W.size(1))
            linear.weight.data = rbm.W.data.t()
            linear.bias.data = rbm.h_bias.data
            layers.append(linear)
            layers.append(nn.ReLU())

        self.feature_extractor = nn.Sequential(*layers)
        self.classifier = nn.Linear(dbn.rbms[-1].W.size(1), num_classes)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.feature_extractor(x)
        return self.classifier(x)


# =====================
# Data (MNIST)
# =====================
transform = transforms.Compose([
    transforms.ToTensor()
])

train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./data', train=True, download=True, transform=transform),
    batch_size=64, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./data', train=False, download=True, transform=transform),
    batch_size=64, shuffle=False)


# =====================
# Train DBN
# =====================
dbn = DBN([784, 256, 128])

dbn.pretrain(train_loader, epochs=3, lr=0.01)


# =====================
# Fine-tuning
# =====================
model = DBNClassifier(dbn).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print("\nFine-tuning classifier...\n")

for epoch in range(5):
    model.train()
    total_loss = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss:.3f}")


# =====================
# Evaluation
# =====================
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"\nTest Accuracy: {100 * correct / total:.2f}%")
