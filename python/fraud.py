# =========================================
# 1. Import libraries
# =========================================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# =========================================
# 2. Load dataset (direct URL)
# =========================================
url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
data = pd.read_csv(url)

print("Dataset loaded!")
print("Shape:", data.shape)
print(data.head())

# =========================================
# 3. Explore imbalance (important!)
# =========================================
print("\nClass distribution:")
print(data["Class"].value_counts())

# =========================================
# 4. Prepare data
# =========================================
X = data.drop("Class", axis=1)
y = data["Class"]  # 0 = normal, 1 = fraud

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================================
# 5. Train model
# =========================================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1   # use all CPU cores
)

model.fit(X_train, y_train)

# =========================================
# 6. Evaluate model
# =========================================
predictions = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# =========================================
# 7. Predict new transaction
# =========================================
# Take a real example from test set
new_transaction = X_test.iloc[0:1]

prediction = model.predict(new_transaction)

print("\nNew Transaction Result:")
if prediction[0] == 1:
    print("Fraud detected!")
else:
    print("Legitimate transaction")

# =========================================
# 8. Feature importance (insight)
# =========================================
import numpy as np

importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

print("\nTop 10 Important Features:")
for i in range(10):
    print(f"{X.columns[indices[i]]}: {importances[indices[i]]:.4f}")
