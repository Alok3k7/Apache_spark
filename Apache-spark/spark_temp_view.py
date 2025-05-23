from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark: SparkSession = SparkSession.builder \
        .appName("hello") \
        .master("local[3]") \
        .getOrCreate()

data = [("Sneha", 28), ("Rahul", 32), ("Priya", 24)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

df.createOrReplaceTempView("people")

result = spark.sql("SELECT * FROM people WHERE Age >= 25")
print("before view")
df.show()
print("after views")
result.show()

spark.stop()
