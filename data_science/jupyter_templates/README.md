# Data Science Jupyter Notebook Templates

This repository contains a collection of reusable Jupyter Notebook templates for common data science tasks, including exploratory data analysis, hypothesis testing, regression analysis, classification, clustering, and machine learning model evaluation.

The templates are designed to help data scientists and analysts quickly develop, execute, and evaluate common data analysis and machine learning workflows using Python.

## Table of Contents

- [Getting Started](#getting-started)
- [Notebook Templates](#notebook-templates)
  - [Exploratory Data Analysis](#1-exploratory-data-analysis-eda)
  - [Hypothesis Testing](#2-basic-hypothesis-testing)
  - [Simple Linear Regression](#3-simple-linear-regression)
  - [Multiple Linear Regression](#4-multiple-linear-regression)
  - [Binomial Logistic Regression](#5-binomial-logistic-regression)
  - [Naive Bayes Classification](#6-naive-bayes-classification)
  - [K-means Clustering](#7-k-means-clustering)
  - [Decision Tree](#8-decision-tree)
  - [Random Forest](#9-random-forest)
  - [Gradient Boosting](#10-gradient-boosting)
  - [Project Notebook](#11-project-notebook)
  - [Model Evaluation](#12-model-evaluation)
- [Technologies and Libraries](#technologies-and-libraries)
- [Getting Help](#getting-help)
- [Contributing](#contributing)

## Getting Started

To use these notebook templates, you need Python and Jupyter Notebook or JupyterLab installed on your machine.

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Jupyter Notebook](https://jupyter.org/install)
- [JupyterLab](https://jupyter.org/)

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/fatvdbergdotus/ai.git
```

Navigate to the Jupyter templates directory:

```bash
cd ai/data_science/jupyter_templates
```

### Run Jupyter Notebook

Start Jupyter Notebook from the directory:

```bash
jupyter notebook
```

Alternatively, launch JupyterLab:

```bash
jupyter lab
```

Open the notebook you want to use and adapt it to your dataset and project requirements.

## Notebook Templates

The repository contains the following Jupyter Notebook templates.

### 1. Exploratory Data Analysis (EDA)

[**01_exploratory_data_analysis.ipynb**](./01_exploratory_data_analysis.ipynb)

This template provides a structured framework for the exploratory data analysis process. It includes code and examples for discovering, structuring, cleaning, joining, validating, and presenting data. It helps identify patterns, detect anomalies, investigate missing values, and understand relationships between variables before applying statistical or machine learning techniques.

### 2. Basic Hypothesis Testing

[**02_hypothesis_test.ipynb**](./02_hypothesis_test.ipynb)

This template provides a starting point for conducting statistical hypothesis tests using Python. It includes examples of statistical z-tests and t-tests, explaining how to formulate null and alternative hypotheses, calculate test statistics and p-values, and interpret the results to determine whether sufficient evidence exists to reject the null hypothesis.

### 3. Simple Linear Regression

[**03_simple_linear_regression.ipynb**](./03_simple_linear_regression.ipynb)

This template provides a starting point for building simple linear regression models in Python. It covers data importing, preprocessing, exploratory analysis, model construction, and performance evaluation. The model investigates the linear relationship between one independent variable and a dependent variable and can be used to understand relationships and make predictions.

### 4. Multiple Linear Regression

[**04_multiple_linear_regression.ipynb**](./04_multiple_linear_regression.ipynb)

This template provides a starting point for building multiple linear regression models in Python. It includes importing and preprocessing data, exploring relationships between variables, constructing a regression model using multiple independent variables, and evaluating model performance. It also provides a framework for understanding how several explanatory variables contribute to predicting a dependent variable.

### 5. Binomial Logistic Regression

[**05_binomial_logistic_regression.ipynb**](./05_binomial_logistic_regression.ipynb)

This template provides a starting point for constructing a binomial logistic regression model in Python. It covers data importing, exploratory data analysis, preprocessing, model construction, and performance evaluation. Logistic regression is used to estimate the probability of an observation belonging to one of two possible classes and is particularly useful for binary classification problems.

### 6. Naive Bayes Classification

[**06_naive_bayes.ipynb**](./06_naive_bayes.ipynb)

This template provides a starting point for constructing a Naive Bayes classification model in Python. It includes loading the required libraries, importing data, performing exploratory data analysis, constructing the classification model, and evaluating the results. Naive Bayes uses Bayes' theorem and assumes conditional independence between predictors given the target class.

### 7. K-means Clustering

[**07_k-means.ipynb**](./07_k-means.ipynb)

This template provides a starting point for constructing a K-means clustering model in Python. It includes importing libraries and data, performing exploratory data analysis, preprocessing and scaling features, constructing the clustering model, and evaluating its performance. K-means is an unsupervised learning algorithm that partitions observations into a predefined number of clusters based on similarity.

### 8. Decision Tree

[**08_decision_tree.ipynb**](./08_decision_tree.ipynb)

This template provides a starting point for constructing a Decision Tree classification model in Python. It includes loading packages, importing data, performing exploratory data analysis, preprocessing, constructing the decision tree, and evaluating the model. Decision trees use a sequence of decision rules to classify observations and provide an interpretable approach to machine learning.

### 9. Random Forest

[**09_random_forest.ipynb**](./09_random_forest.ipynb)

This template provides a starting point for constructing a Random Forest classification model in Python. It includes loading packages, importing data, performing exploratory data analysis, constructing the model, and evaluating its performance. Random Forest combines multiple decision trees using ensemble learning to improve predictive performance and reduce overfitting compared with individual decision trees.

### 10. Gradient Boosting

[**10_gradient_boosting.ipynb**](./10_gradient_boosting.ipynb)

This template provides a starting point for constructing a Gradient Boosting classification model in Python. It includes loading packages, importing data, performing exploratory data analysis, constructing the model, and evaluating its performance. Gradient Boosting builds an ensemble of sequentially trained weak learners, with each subsequent learner attempting to correct errors made by previous learners.

### 11. Project Notebook

[**11_project_notebook.ipynb**](./11_project_notebook.ipynb)

This notebook provides a general-purpose project template designed to improve the structure and logical workflow of data science projects. It offers a starting point for organizing project objectives, data acquisition, data preparation, exploratory analysis, modelling, evaluation, and conclusions in a consistent and reproducible manner.

### 12. Model Evaluation

[**12_model_evaluation.ipynb**](./12_model_evaluation.ipynb)

This notebook provides reusable functions that support a train-validation-test approach to model development. The functions make it easier to inspect model results at different stages of the development process and aggregate evaluation results into a Pandas DataFrame for systematic model comparison. It provides a consistent framework for assessing and comparing the performance of different machine learning models.

## Technologies and Libraries

The notebooks use Python and commonly adopted data science and machine learning libraries.

| Technology / Library | Purpose | Documentation |
|---|---|---|
| Python | Programming language | [Documentation](https://docs.python.org/3/) |
| Jupyter | Interactive notebooks | [Documentation](https://docs.jupyter.org/) |
| NumPy | Numerical computing | [Documentation](https://numpy.org/doc/) |
| Pandas | Data manipulation and analysis | [Documentation](https://pandas.pydata.org/docs/) |
| Matplotlib | Data visualization | [Documentation](https://matplotlib.org/stable/) |
| Seaborn | Statistical data visualization | [Documentation](https://seaborn.pydata.org/) |
| SciPy | Scientific and statistical computing | [Documentation](https://docs.scipy.org/doc/scipy/) |
| Statsmodels | Statistical modelling and hypothesis testing | [Documentation](https://www.statsmodels.org/) |
| Scikit-learn | Machine learning | [Documentation](https://scikit-learn.org/stable/) |

## Getting Help

The following resources provide additional information about the technologies and methods used in the notebooks:

- [Python Documentation](https://docs.python.org/3/)
- [Jupyter Documentation](https://docs.jupyter.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [Statsmodels Documentation](https://www.statsmodels.org/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
