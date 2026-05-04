(c) 2026 Freek van den Berg. All rights reserved.

## 🎯 Target Encoding Example

### Original Dataset

| Customer_ID | City     | Purchased (Target) |
|------------|----------|--------------------|
| 1          | Amsterdam| 1                  |
| 2          | Rotterdam| 0                  |
| 3          | Amsterdam| 1                  |
| 4          | Utrecht  | 0                  |
| 5          | Rotterdam| 1                  |
| 6          | Utrecht  | 0                  |

---

### Step 1: Compute Target Mean per Category

We calculate the average of the target variable for each city:

| City      | Mean(Target) |
|-----------|-------------|
| Amsterdam | (1 + 1) / 2 = 1.0 |
| Rotterdam | (0 + 1) / 2 = 0.5 |
| Utrecht   | (0 + 0) / 2 = 0.0 |

---

### Step 2: Replace Categories with Target Mean

| Customer_ID | City (Encoded) | Purchased |
|------------|----------------|-----------|
| 1          | 1.0            | 1         |
| 2          | 0.5            | 0         |
| 3          | 1.0            | 1         |
| 4          | 0.0            | 0         |
| 5          | 0.5            | 1         |
| 6          | 0.0            | 0         |

---

## ⚠️ Important Notes

- This encoding introduces **target information into features**
- Must avoid **data leakage**:
  - Use cross-validation (out-of-fold encoding)
  - Or apply smoothing

---

## 🧠 Smoothed Target Encoding (Optional)

To reduce overfitting:

\[
Encoded = \frac{(mean \times count) + (global\_mean \times k)}{count + k}
\]

Where:
- `mean` = category mean  
- `count` = number of samples in category  
- `global_mean` = overall target mean  
- `k` = smoothing parameter  

---

## ✅ When to Use

- High-cardinality categorical features  
- Tree-based models (e.g., Random Forest, XGBoost)  
- When one-hot encoding becomes too large  
