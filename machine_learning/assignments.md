# Machine Learning Assignments

## ARIMA, SARIMA and SARIMAX
Forecasting is applied to daily business performance data (revenue, discount rate, and coupon rate over time). The goal is to predict future revenue based on historical patterns and possibly the influence of pricing strategies like discounts and coupons. A basic approach would use ARIMA to model revenue purely from its past values, capturing trends and short-term dependencies. If your data shows recurring patterns (e.g., weekly or monthly sales cycles), SARIMA would be more appropriate because it accounts for seasonality. Since your dataset also includes variables like discount rate and coupon rate—which directly affect revenue—a SARIMAX model is the most suitable, as it can incorporate these external factors to improve forecast accuracy. This allows you not only to predict future revenue but also to understand how pricing strategies impact sales over time, making it valuable for business planning and optimization.

Jupyter Notebook: [ARIMA, SARIMA and SARIMAX.ipynb](/python/ARIMA,%20SARIMA%20and%20SARIMAX.ipynb)

Dataset files: [daily_revenue.csv](/python/daily_revenue.csv) and [future_regressors.csv](/python/future_regressors.csv)

## Decision Trees
Decision Trees are a widely used method in Machine Learning for both classification and regression tasks, where data is split into branches based on feature values to make predictions in a clear, rule-based structure. The model works by recursively selecting the best feature to divide the dataset—using criteria such as information gain or Gini impurity—until it reaches decision nodes that produce final outputs. For example, a decision tree for loan approval might first split applicants based on income level, then credit score, and finally employment status to determine whether to approve or reject the loan. Decision trees are highly interpretable because their flowchart-like structure makes it easy to understand how decisions are made, but they can be prone to overfitting if the tree becomes too complex, which is why techniques like pruning or combining multiple trees (as in random forests) are often used to improve performance.

Python code: [Decision Trees](/python/SparkDecisionTree.py)

## K-Nearest Neighbour
K-Nearest Neighbour (KNN) is a simple yet powerful algorithm in Machine Learning used for both classification and regression tasks, based on the idea that similar data points tend to be close to each other in feature space. Instead of building an explicit model, KNN stores the training data and makes predictions by identifying the “K” closest data points (neighbors) to a given input using a distance metric such as Euclidean distance, then assigning the most common class (for classification) or averaging the values (for regression). For example, in a classification problem like email spam detection, KNN can classify a new email by comparing it to the most similar previously labeled emails and assigning the majority label. While KNN is easy to understand and implement, it can become computationally expensive with large datasets and is sensitive to the choice of K and the scaling of features, which can significantly influence its performance.

Python code: [KNN](/python/KNN.ipynb)

## K-Means Clustering
K-Means Clustering is a popular unsupervised learning algorithm in Machine Learning used to group data points into a predefined number of clusters based on similarity. The algorithm works by initializing K centroids, assigning each data point to the nearest centroid, and then iteratively updating the centroids by calculating the mean of the assigned points until the clusters stabilize. For example, a company might use K-Means to segment customers into groups based on purchasing behavior, such as high spenders, occasional buyers, and discount seekers. It is widely used in applications like image compression, market segmentation, and pattern recognition due to its simplicity and efficiency. However, K-Means requires the number of clusters to be specified in advance and can be sensitive to the initial placement of centroids, which may affect the final results.

Python code: [K-Means](/python/KMeans.ipynb) [Spark K-Means](/python/SparkKMeans.py) [Manual k-means](/python/Kmeans_manual.py)

## Linear/Logistic Regression
Linear and Logistic Regression are fundamental techniques in Machine Learning used for prediction and classification tasks. Linear Regression is used to model the relationship between a dependent variable and one or more independent variables by fitting a straight line to the data, typically expressed as a weighted sum of inputs; for example, it can predict house prices based on features like size and location. In contrast, Logistic Regression is used for classification problems, where the output is categorical (such as yes/no or 0/1), and it applies a sigmoid function to map predictions to probabilities between 0 and 1, making it suitable for tasks like spam detection or disease diagnosis. While Linear Regression focuses on predicting continuous values, Logistic Regression estimates the likelihood of a particular class, and both methods are widely valued for their simplicity, interpretability, and effectiveness as baseline models in data analysis and predictive modeling.

Python code: [Linear Regression](/python/LinearRegression.ipynb)

## Multiple Regression
Multiple regression is a statistical method used to understand how one outcome (called the dependent variable) is influenced by two or more predictors (independent variables) at the same time. Instead of looking at relationships one-by-one, it allows you to see the combined effect of several factors while holding the others constant—for example, predicting house prices based on size, location, and number of rooms simultaneously. The model fits an equation of the form Y = b₀ + b₁X₁ + b₂X₂ + … + bₙXₙ + error, where each coefficient (b) represents how much the dependent variable changes when that specific predictor increases by one unit, assuming all other variables stay the same. This makes multiple regression especially powerful for real-world situations where outcomes are influenced by many interacting factors, helping identify which variables matter most and how strongly they contribute.

Python code: [Multiple Regression](/python/MultipleRegression.ipynb)

## Principal Component Analysis
Principal Component Analysis (PCA) is a widely used dimensionality reduction technique in Machine Learning that transforms high-dimensional data into a smaller set of uncorrelated variables called principal components while preserving as much variance as possible. It works by identifying directions (components) along which the data varies the most and projecting the original data onto these directions, effectively simplifying complex datasets without losing significant information. For example, in image processing, PCA can reduce the number of features (pixels) needed to represent an image while retaining its essential structure, and in finance, it can be used to identify key factors influencing stock price movements. By reducing dimensionality, PCA helps improve computational efficiency, reduce noise, and enhance visualization, making it an essential tool for preprocessing and exploratory data analysis in many real-world applications.

Python code: [PCA](/python/PCA.ipynb) [Spark PCA](/python/SparkPCA.py)

## Polynomial Regression
**Polynomial regression** is a type of regression analysis used to model relationships between variables when the pattern is **nonlinear** but can still be expressed as a curved equation. Instead of fitting a straight line (as in linear regression), it fits a polynomial equation such as:

y = b₀ + b₁x + b₂x² + b₃x³ + … + bₙxⁿ

Here, the independent variable (x) is raised to higher powers, allowing the model to capture curves, bends, and more complex trends in the data. Even though the relationship appears nonlinear, the model is still considered “linear” in terms of its coefficients, because it estimates them in a linear way. Polynomial regression is useful when data shows patterns like acceleration, peaks, or diminishing returns—for example, modeling growth rates or physical motion—while still remaining relatively simple compared to more advanced nonlinear models; however, choosing too high a degree can lead to overfitting, where the model captures noise instead of the true underlying pattern.

Python code: [Polynomial Regression](/python/PolynomialRegression.ipynb) 

## Q-Learning

Q-learning is a reinforcement learning algorithm used in artificial intelligence to help an agent learn the best actions to take in an environment. It is a **model-free** method, meaning the agent does not need prior knowledge of the environment and instead learns through trial and error.

The main idea of Q-learning is the **Q-value (quality value)**, which represents how good a particular action is in a given state. The agent explores different actions, receives rewards or penalties, and updates its Q-values over time to improve its decisions.

### Q-Learning Update Rule

Q(s, a) = Q(s, a) + α [ r + γ max Q(s', a') − Q(s, a) ]

Where:
**s** = current state, **a** = action taken, **r** = reward received, **s'** = next state, **α (alpha)** = learning rate and **γ (gamma)** = discount factor  

Applications: Game playing, Robotics, Navigation systems and Decision-making problems  

Q-learning is powerful because it can learn optimal strategies even when the environment is unknown or uncertain.

Python code: [Q-learning](/python/Q-Learning.ipynb)

## Random Forest
Random Forest is an advanced ensemble method in Machine Learning that builds multiple decision trees and combines their outputs to improve prediction accuracy and reduce overfitting. Instead of relying on a single tree, the algorithm creates many trees using different subsets of the training data and randomly selected features, a technique known as bagging (bootstrap aggregating). Each tree makes its own prediction, and the final result is determined by majority voting (for classification) or averaging (for regression). For example, in a medical diagnosis system, different trees might analyze various combinations of symptoms and patient data, and the forest aggregates their predictions to produce a more reliable diagnosis. Random Forest models are powerful because they handle large datasets, capture complex patterns, and are less sensitive to noise compared to individual decision trees, though they can be more computationally intensive and less interpretable due to their ensemble nature.

[Random forest manual](/python/random_forest_manual.py) [Random forest scikit-learn](/python/random_forest.py)

## Support Vector Machines
In machine learning, support vector machines (SVMs, also support vector networks) are supervised max-margin models with associated learning algorithms that analyze data for classification and regression analysis. Developed at AT&T Bell Laboratories, SVMs are one of the most studied models, being based on statistical learning frameworks of VC theory proposed by Vapnik (1982, 1995) and Chervonenkis (1974).

In addition to performing linear classification, SVMs can efficiently perform non-linear classification using the kernel trick, representing the data only through a set of pairwise similarity comparisons between the original data points using a kernel function, which transforms them into coordinates in a higher-dimensional feature space. Thus, SVMs use the kernel trick to implicitly map their inputs into high-dimensional feature spaces, where linear classification can be performed. Being max-margin models, SVMs are resilient to noisy data (e.g., misclassified examples). SVMs can also be used for regression tasks, where the objective becomes ϵ-sensitive.

The support vector clustering algorithm, created by Hava Siegelmann and Vladimir Vapnik, applies the statistics of support vectors, developed in the support vector machines algorithm, to categorize unlabeled data. These data sets require unsupervised learning approaches, which attempt to find natural clustering of the data into groups, and then to map new data according to these clusters.

The popularity of SVMs is likely due to their amenability to theoretical analysis, and their flexibility in being applied to a wide variety of tasks, including structured prediction problems. It is not clear that SVMs have better predictive performance than other linear models, such as logistic regression and linear regression.

Related Python: [SVM](/python/SVC.ipynb)

## TFT Electricity case
A Temporal Fusion Transformer (TFT) can be used in electricity demand forecasting to predict future power consumption across multiple time horizons by learning from historical usage patterns and external variables. For example, a utility company can train a TFT model on past electricity load data along with time-dependent features such as temperature, humidity, day of the week, and holiday indicators. The model captures both short-term fluctuations (like hourly demand spikes) and long-term trends (such as seasonal variation), while its attention mechanisms highlight which factors are most influential at different times. This enables accurate and interpretable forecasts that help grid operators balance supply and demand, optimize energy distribution, and reduce operational costs.

Python: [TFT project freek.ipynb](/python/TFT%20project%20freek.ipynb)

Datasets: [electricity.csv](/python/electricity.csv) and [electricity-future.csv](/python/electricity-future.csv)
