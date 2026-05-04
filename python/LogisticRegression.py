from sklearn.linear_model import LogisticRegression

# Create the model
# Example data (2 features)
X = [ [2, 3], [1, 1], [3, 2], [8, 7], [9, 8], [7, 9] ]
y = [0, 0, 0, 1, 1, 1]  # binary labels

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
probabilities = model.predict_proba(X)

print("Predictions:", predictions)
print("Probabilities:", probabilities)

# Apply the model to new cases
# New unseen data
new_data = [
    [2, 2],   # likely class 0
    [8, 8],   # likely class 1
    [5, 5]    # uncertain
]

# Predict class labels
new_predictions = model.predict(new_data)

# Predict probabilities
new_probabilities = model.predict_proba(new_data)

print("New Predictions:", new_predictions)
print("New Probabilities:", new_probabilities)


# Output
# Predictions: [0 0 0 1 1 1]
# Probabilities: [[0.95147301 0.04852699]
 # [0.99107993 0.00892007]
 # [0.951071   0.048929  ]
 # [0.05576457 0.94423543]
 # [0.01818996 0.98181004]
 # [0.03242468 0.96757532]]
# New Predictions: [0 1 0]
# New Probabilities: [[0.97210999 0.02789001]
 # [0.03215369 0.96784631]
 # [0.5183236  0.4816764 ]]
