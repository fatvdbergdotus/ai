import random
from collections import Counter

# --- Decision Tree (very simplified) ---
class DecisionTree:
    def __init__(self, max_depth=5, min_samples_split=2, n_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.n_features = n_features
        self.tree = None

    def fit(self, X, y):
        self.n_features = self.n_features or len(X[0])
        self.tree = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        num_samples = len(y)
        num_labels = len(set(y))

        # stopping criteria
        if (depth >= self.max_depth or
            num_labels == 1 or
            num_samples < self.min_samples_split):
            return self._most_common_label(y)

        feat_idxs = random.sample(range(len(X[0])), self.n_features)

        # find best split
        best_feat, best_thresh = self._best_split(X, y, feat_idxs)

        left_idxs, right_idxs = self._split(X, best_feat, best_thresh)

        left = self._grow_tree([X[i] for i in left_idxs], [y[i] for i in left_idxs], depth+1)
        right = self._grow_tree([X[i] for i in right_idxs], [y[i] for i in right_idxs], depth+1)

        return (best_feat, best_thresh, left, right)

    def _best_split(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_thresh = None, None

        for feat in feat_idxs:
            values = [x[feat] for x in X]
            thresholds = set(values)

            for t in thresholds:
                gain = self._information_gain(y, values, t)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat
                    split_thresh = t

        return split_idx, split_thresh

    def _information_gain(self, y, values, threshold):
        def gini(labels):
            counts = Counter(labels)
            impurity = 1
            for c in counts.values():
                prob = c / len(labels)
                impurity -= prob ** 2
            return impurity

        left = [y[i] for i in range(len(y)) if values[i] <= threshold]
        right = [y[i] for i in range(len(y)) if values[i] > threshold]

        if not left or not right:
            return 0

        n = len(y)
        gain = gini(y) - (len(left)/n)*gini(left) - (len(right)/n)*gini(right)
        return gain

    def _split(self, X, feat, thresh):
        left, right = [], []
        for i, x in enumerate(X):
            if x[feat] <= thresh:
                left.append(i)
            else:
                right.append(i)
        return left, right

    def _most_common_label(self, y):
        return Counter(y).most_common(1)[0][0]

    def predict(self, X):
        return [self._traverse_tree(x, self.tree) for x in X]

    def _traverse_tree(self, x, node):
        if not isinstance(node, tuple):
            return node

        feat, thresh, left, right = node
        if x[feat] <= thresh:
            return self._traverse_tree(x, left)
        return self._traverse_tree(x, right)


# --- Random Forest ---
class RandomForest:
    def __init__(self, n_trees=5, max_depth=5):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            # bootstrap sample
            indices = [random.randint(0, len(X)-1) for _ in range(len(X))]
            X_sample = [X[i] for i in indices]
            y_sample = [y[i] for i in indices]

            tree = DecisionTree(max_depth=self.max_depth,
                                n_features=int(len(X[0])**0.5))
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def predict(self, X):
        tree_preds = [tree.predict(X) for tree in self.trees]
        tree_preds = list(zip(*tree_preds))

        return [Counter(preds).most_common(1)[0][0] for preds in tree_preds]


# --- Example usage ---
X = [
    [2, 3], [1, 1], [3, 2],
    [8, 7], [9, 8], [7, 9]
]
y = [0, 0, 0, 1, 1, 1]

rf = RandomForest(n_trees=5, max_depth=3)
rf.fit(X, y)

predictions = rf.predict(X)
print("Predictions:", predictions)
