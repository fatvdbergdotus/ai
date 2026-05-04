import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def mean(points):
    return [sum(dim) / len(points) for dim in zip(*points)]

def kmeans(data, k, max_iters=100):
    # Step 1: randomly initialize centroids
    centroids = random.sample(data, k)

    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]

        # Step 2: assign points to nearest centroid
        for point in data:
            distances = [euclidean_distance(point, c) for c in centroids]
            closest_index = distances.index(min(distances))
            clusters[closest_index].append(point)

        # Step 3: recompute centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:  # avoid empty cluster
                new_centroids.append(mean(cluster))
            else:
                new_centroids.append(random.choice(data))

        # Step 4: check for convergence
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids, clusters


# Example usage
data = [(1, 2), (2, 1), (8, 9), (9, 8), (1, 1), (8, 8)]
centroids, clusters = kmeans(data, k=2)

print("Centroids:", centroids)
print("Clusters:", clusters)
