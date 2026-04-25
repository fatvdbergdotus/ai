# Assignment 1: mammogram-detected mass
This assignment involves building a machine learning model to predict whether a mammogram-detected mass is benign or malignant using a public dataset of 961 cases. The dataset includes features such as patient age, mass shape, margin, and density, while the BI-RADS assessment is excluded since it reflects diagnostic confidence rather than predictive value. The goal is to use these features to predict the “severity” (benign or malignant). Because medical misdiagnoses—especially false positives—can lead to unnecessary stress and procedures, improving prediction accuracy through machine learning has real-world importance.

To complete the project, you must clean and prepare the dataset (handling missing values and potential outliers), then apply multiple supervised learning algorithms: Decision Tree, Random Forest, K-Nearest Neighbors, Naive Bayes, Support Vector Machine, and Logistic Regression. Each model should be evaluated using 10-fold cross-validation, and you are encouraged to tune hyperparameters to improve performance. The benchmark is around 80% accuracy, and the objective is to determine which method performs best while demonstrating proper data preprocessing, model training, and evaluation techniques.

Python Notebook code: [Code](/python/FinalProjectAssignment.ipynb)


# Assignment 2: Fertility-related health and lifestyle indicators
This synthetic dataset contains fertility-related health and lifestyle indicators for couples. It includes female and male age, BMI, menstrual regularity, PCOS status, sperm count, sperm motility, stress levels, sleep quality, smoking habits, alcohol intake, and exercise levels. The dataset is designed for machine learning tasks such as predicting pregnancy outcomes (Success / Failure), and is fully anonymized for research and educational purposes.

The dataset is from [https://www.kaggle.com/datasets/shauryasrivastava01/fertility-health-dataset](https://www.kaggle.com/datasets/shauryasrivastava01/fertility-health-dataset)

Jupyter Notebook: [Fertility](fertility.ipynb)

CSV file: [CSV](fertility_health_dataset.csv)


# Assignment 3: Titanic survival

Used files:
- [gender_submission.csv](gender_submission.csv)
- [test.csv](test.csv)
- [train.csv](train.csv)

Jupyter Notebook:
- [titanic.ipynb](titanic.ipynb)
- [titanic_varying_using_features.ipynb](titanic_varying_using_features.ipynb)
- [titanic_pca.ipynb](titanic_pca.ipynb)

# Assignment 4: Classifying Cats and Dogs images
The Cat and Dog Classification dataset is a standard computer vision dataset that involves classifying photos as either containing a dog or a cat. This dataset is provided as a subset of photos from a much larger dataset of approximately 25 thousands.

The dataset contains 24,998 images, split into 12,499 Cat images and 12,499 Dog images. The training images are divided equally between cat and dog images, while the test images are not labeled. This allows users to evaluate their models on unseen data.

Used files:
- [cats_vs_dogs.ipynb](cats_vs_dogs.ipynb)
