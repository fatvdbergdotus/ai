| Encoding Technique | Linear Models (LR, Logistic) | Tree-Based Models (RF, XGBoost) | SVM | Neural Networks | Naive Bayes | Transformers (BERT, GPT) |
|-------------------|-----------------------------|----------------------------------|-----|------------------|-------------|--------------------------|
| One-hot encoding  | ✅ Excellent                | ✅ Good                         | ✅ Good | ⚠️ OK (high dim) | ❌ Not ideal | ❌ Not used              |
| Label encoding    | ❌ Risky (false order)      | ✅ OK                           | ❌ Bad | ⚠️ Sometimes     | ❌ Bad       | ❌ Not used              |
| TF-IDF            | ✅ Excellent                | ⚠️ OK                           | ✅ Excellent | ⚠️ Rare        | ✅ Excellent | ❌ Not used              |
| Bag-of-Words      | ✅ Good                     | ⚠️ OK                           | ✅ Good | ⚠️ Rare        | ✅ Excellent | ❌ Not used              |
| Embeddings        | ⚠️ Rare                     | ❌ Poor                         | ⚠️ Rare | ✅ Best        | ❌ Not used  | ✅ Built-in              |
| Tokenization      | ❌ No                       | ❌ No                           | ❌ No  | ✅ Required (NLP) | ❌ No        | ✅ Required              |
| Raw text          | ❌ No                       | ❌ No                           | ❌ No  | ❌ No           | ❌ No        | ❌ No (needs tokens)     |
