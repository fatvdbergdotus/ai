(c) 2026 Freek van den Berg. All rights reserved.

# Decision Trees
Decision Trees are a widely used method in Machine Learning for both classification and regression tasks, where data is split into branches based on feature values to make predictions in a clear, rule-based structure. The model works by recursively selecting the best feature to divide the dataset—using criteria such as information gain or Gini impurity—until it reaches decision nodes that produce final outputs. For example, a decision tree for loan approval might first split applicants based on income level, then credit score, and finally employment status to determine whether to approve or reject the loan. Decision trees are highly interpretable because their flowchart-like structure makes it easy to understand how decisions are made, but they can be prone to overfitting if the tree becomes too complex, which is why techniques like pruning or combining multiple trees (as in random forests) are often used to improve performance.

Python code: [Decision Trees](/python/SparkDecisionTree.py)
