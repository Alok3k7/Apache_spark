from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("hello") \
        .master("local[3]") \
        .getOrCreate()

    df = spark.read \
        .format("json") \
        .option("path", "/home/alok/Downloads/spark.json") \
        .load()

    df1 = df.repartition(2)

    df.show()
    df1.show()
