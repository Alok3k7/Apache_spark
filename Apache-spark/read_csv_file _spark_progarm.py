from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("hello") \
        .master("local[3]") \
        .getOrCreate()

    df = spark.read \
        .format("csv") \
        .option("path", "/home/alok/Downloads/organizations-100.csv") \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .load()

    df1 = df.repartition(2)

    df.show()
    df1.show()

    filter_df = df1 \
        .where("`Number of employees` < 3000") \
        .select("Index", "Country", "Founded", "Number of employees", "Name")

    groupby_df = df1 \
        .groupBy("Founded") \
        .count()

    groupby_df.show()
    filter_df.show()

input("press enter")
