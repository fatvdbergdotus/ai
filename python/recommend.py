# =========================================
# 1. Import libraries
# =========================================
import pandas as pd

# =========================================
# 2. Load datasets (direct URLs)
# =========================================
ratings_url = "https://files.grouplens.org/datasets/movielens/ml-latest-small/ratings.csv"
movies_url = "https://files.grouplens.org/datasets/movielens/ml-latest-small/movies.csv"

ratings = pd.read_csv(ratings_url)
movies = pd.read_csv(movies_url)

print("Ratings sample:")
print(ratings.head())

print("\nMovies sample:")
print(movies.head())

# =========================================
# 3. Merge datasets
# =========================================
data = pd.merge(ratings, movies, on="movieId")

# =========================================
# 4. Create user-movie matrix
# =========================================
user_movie_matrix = data.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)

print("\nMatrix shape:", user_movie_matrix.shape)

# =========================================
# 5. Compute similarity between movies
# =========================================
movie_similarity = user_movie_matrix.corr(method="pearson")

# =========================================
# 6. Recommendation function
# =========================================
def recommend(movie_name, min_ratings=50):
    if movie_name not in movie_similarity.columns:
        return f"Movie '{movie_name}' not found in dataset."

    similar_scores = movie_similarity[movie_name].dropna()

    # Count how many ratings each movie has
    rating_counts = data.groupby("title")["rating"].count()

    # Filter out unpopular movies
    similar_scores = similar_scores[rating_counts > min_ratings]

    # Sort by similarity
    recommendations = similar_scores.sort_values(ascending=False)

    return recommendations.head(10)

# =========================================
# 7. Test recommendation
# =========================================
movie_name = "Toy Story (1995)"

print(f"\nRecommendations for: {movie_name}\n")
print(recommend(movie_name))
