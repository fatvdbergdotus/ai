## Backpropagation in Neural Networks

Backpropagation (short for *backward propagation of errors*) is an algorithm used to train neural networks by adjusting weights to minimize prediction errors.

In a neural network, data first passes through the layers in a **forward pass**, producing an output. This output is compared with the actual target using a loss function to calculate the error. Backpropagation then sends this error backward through the network to determine how much each weight contributed to the error.

The algorithm uses the **chain rule from calculus** to compute gradients (partial derivatives) of the loss function with respect to each weight. These gradients are then used to update the weights and reduce the error.

### Weight Update Rule

w = w − η (∂L / ∂w)

Where:
- **w** = weight  
- **η (eta)** = learning rate  
- **∂L / ∂w** = gradient of the loss function  

### Key Points
- Involves a **forward pass** and a **backward pass**  
- Uses **gradient descent** to update weights  
- Aims to **minimize the loss function**  

### Applications
- Image recognition  
- Speech recognition  
- Natural language processing  
- Deep learning systems  

Backpropagation is essential for enabling neural networks to learn from data.
