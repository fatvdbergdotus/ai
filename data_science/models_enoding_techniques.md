(c) 2026 Freek van den Berg. All rights reserved.

| Encoding Technique | Linear Regression | Logistic Regression | K-Means | DBSCAN | Naive Bayes | Random Forest | XGBoost | ARIMA |
|-------------------|------------------|---------------------|---------|--------|-------------|---------------|---------|--------|
| One-hot encoding  | ✅ Excellent     | ✅ Excellent        | ⚠️ OK (high dim) | ⚠️ OK (distance issues) | ❌ Not ideal | ✅ Good | ✅ Good | ❌ Not used |
| Label encoding    | ❌ Risky         | ❌ Risky            | ❌ Bad (fake order) | ❌ Bad | ❌ Bad | ✅ OK | ✅ OK | ❌ Not used |
| Binary encoding   | ✅ Good          | ✅ Good             | ✅ Good | ✅ Good | ❌ Not ideal | ✅ Good | ✅ Good | ❌ Not used |
| Base-N encoding   | ✅ Good          | ✅ Good             | ✅ Good | ✅ Good | ❌ Not ideal | ✅ Good | ✅ Good | ❌ Not used |
| Hash encoding     | ✅ Good          | ✅ Good             | ⚠️ OK (collisions) | ⚠️ OK | ❌ Not ideal | ✅ Good | ✅ Good | ❌ Not used |
| Target encoding   | ⚠️ Risky         | ⚠️ Risky            | ❌ Not suitable | ❌ Not suitable | ❌ Not ideal | ✅ Excellent | ✅ Excellent | ❌ Not used |
| TF-IDF            | ⚠️ Rare          | ⚠️ Rare             | ⚠️ Rare | ⚠️ Rare | ✅ Excellent | ⚠️ Rare | ⚠️ Rare | ❌ Not used |
| Bag-of-Words      | ⚠️ Rare          | ⚠️ Rare             | ⚠️ Rare | ⚠️ Rare | ✅ Excellent | ⚠️ Rare | ⚠️ Rare | ❌ Not used |
| Embeddings        | ⚠️ Rare          | ⚠️ Rare             | ✅ Good | ✅ Good | ❌ Not used | ❌ Poor | ❌ Poor | ❌ Not used |
| Tokenization      | ❌ No            | ❌ No               | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| Raw text          | ❌ No            | ❌ No               | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
