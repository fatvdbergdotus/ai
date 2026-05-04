# =========================================
# 1. Start Spark Session
# =========================================
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MovieRecommender") \
    .getOrCreate()

# =========================================
# 2. Load Data (can scale to GBs/TBs)
# =========================================
ratings = spark.read.csv(
    "https://files.grouplens.org/datasets/movielens/ml-latest/ratings.csv",
    header=True,
    inferSchema=True
)

movies = spark.read.csv(
    "https://files.grouplens.org/datasets/movielens/ml-latest/movies.csv",
    header=True,
    inferSchema=True
)

ratings.printSchema()
movies.printSchema()

# =========================================
# 3. Data Preparation
# =========================================
from pyspark.sql.functions import col

ratings = ratings.select(
    col("userId").cast("int"),
    col("movieId").cast("int"),
    col("rating").cast("float")
)

# =========================================
# 4. Train/Test Split
# =========================================
(train, test) = ratings.randomSplit([0.8, 0.2])

# =========================================
# 5. Build ALS Model (distributed)
# =========================================
from pyspark.ml.recommendation import ALS

als = ALS(
    userCol="userId",
    itemCol="movieId",
    ratingCol="rating",
    coldStartStrategy="drop",   # avoids NaN
    nonnegative=True
)

model = als.fit(train)

# =========================================
# 6. Evaluate Model
# =========================================
from pyspark.ml.evaluation import RegressionEvaluator

predictions = model.transform(test)

evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="rating",
    predictionCol="prediction"
)

rmse = evaluator.evaluate(predictions)
print("RMSE:", rmse)

# =========================================
# 7. Generate Recommendations
# =========================================

# Top 10 movies for each user
user_recs = model.recommendForAllUsers(10)

# Top 10 users for each movie
movie_recs = model.recommendForAllItems(10)

user_recs.show(5, truncate=False)

# =========================================
# 8. Join with Movie Titles (Readable Output)
# =========================================
from pyspark.sql.functions import explode

exploded = user_recs.select(
    col("userId"),
    explode(col("recommendations")).alias("rec")
)

final_recs = exploded.select(
    "userId",
    col("rec.movieId"),
    col("rec.rating")
).join(movies, "movieId")

final_recs.show(10)

# =========================================
# 9. Stop Spark
# =========================================
spark.stop()
