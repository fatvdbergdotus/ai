from sklearn.ensemble import RandomForestClassifier

# Example data
X = [
    [2, 3], [1, 1], [3, 2],
    [8, 7], [9, 8], [7, 9]
]
y = [0, 0, 0, 1, 1, 1]

# Create model
model = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)

# Train model
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

print("Predictions:", predictions)
