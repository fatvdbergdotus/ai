# automatic_reasoning_demo.py

# -----------------------------
# 1. Rule-based reasoning
# -----------------------------
def recommend_action(weather, temperature):
    if weather == "rainy":
        return "Take an umbrella"
    elif weather == "sunny" and temperature > 25:
        return "Wear sunglasses"
    elif weather == "cold":
        return "Wear a jacket"
    else:
        return "Have a nice day!"


# -----------------------------
# 2. Knowledge-based reasoning
# -----------------------------
def decide(facts):
    if facts.get("raining") and not facts.get("have_umbrella"):
        return "Stay inside or buy an umbrella"
    elif facts.get("raining"):
        return "Go outside with umbrella"
    else:
        return "Go outside"


# -----------------------------
# 3. Inference engine
# -----------------------------
def infer(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for condition, result in rules:
            if condition in inferred and result not in inferred:
                inferred.add(result)
                changed = True

    return inferred


# -----------------------------
# 4. Machine learning reasoning
# -----------------------------
def ml_example():
    try:
        from sklearn.tree import DecisionTreeClassifier
    except ImportError:
        print("\n[ML] scikit-learn not installed. Skipping ML example.")
        return

    # Training data: [temperature, weather_code]
    # weather_code: 0 = sunny, 1 = rainy
    X = [[30, 0], [10, 1], [25, 0], [8, 1]]
    y = ["sunglasses", "umbrella", "sunglasses", "umbrella"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    prediction = model.predict([[20, 0]])
    print("\n[ML] Prediction for (20°C, sunny):", prediction[0])


# -----------------------------
# Main demo
# -----------------------------
def main():
    print("=== AUTOMATIC REASONING DEMO ===")

    # 1. Rule-based
    print("\n[Rule-based]")
    action = recommend_action("sunny", 30)
    print("Recommendation:", action)

    # 2. Knowledge-based
    print("\n[Knowledge-based]")
    facts = {"raining": True, "have_umbrella": False}
    decision = decide(facts)
    print("Decision:", decision)

    # 3. Inference engine
    print("\n[Inference engine]")
    rules = [
        ("raining", "wet_ground"),
        ("wet_ground", "slippery"),
        ("slippery", "walk_carefully")
    ]

    facts = {"raining"}
    inferred = infer(facts, rules)
    print("Inferred knowledge:", inferred)

    # 4. Machine learning
    print("\n[Machine Learning]")
    ml_example()


if __name__ == "__main__":
    main()


'''
OUTPUT


Run started
Initializing environment
Installing packages
Running code
=== AUTOMATIC REASONING DEMO ===


[Rule-based]
Recommendation: Wear sunglasses


[Knowledge-based]
Decision: Stay inside or buy an umbrella


[Inference engine]
Inferred knowledge: {'wet_ground', 'walk_carefully', 'raining', 'slippery'}


[Machine Learning]

[ML] Prediction for (20°C, sunny):
 sunglasses

Run completed in 6728.900000095367ms
'''
