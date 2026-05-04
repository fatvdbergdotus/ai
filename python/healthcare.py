# =========================
# 1. Import libraries
# =========================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =========================
# 2. Load dataset (direct URL)
# =========================
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
data = pd.read_csv(url)

# Preview data
print("First 5 rows:")
print(data.head())

# =========================
# 3. Prepare data
# =========================
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 4. Train model
# =========================
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# =========================
# 5. Evaluate model
# =========================
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

# =========================
# 6. Test on new patient
# =========================
# Format: [Pregnancies, Glucose, BloodPressure, SkinThickness,
#          Insulin, BMI, DiabetesPedigreeFunction, Age]

new_patient = [[2, 120, 70, 20, 85, 30.5, 0.5, 45]]

prediction = model.predict(new_patient)

print("\nNew Patient Prediction:")
print("Diabetes Risk:", "High" if prediction[0] == 1 else "Low")
