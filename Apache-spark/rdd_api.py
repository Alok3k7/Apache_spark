from pyspark import SparkConf
from pyspark.sql import SparkSession

from pyspark.sql.functions import col

if __name__ == "__main__":
    conf = (SparkConf()
            .setMaster("local[3]")
            .setAppName("HelloRDD"))

    spark = (SparkSession
             .builder
             .config(conf=conf)
             .getOrCreate())

    sc = spark.sparkContext

    df = spark.read \
        .format("csv") \
        .option("path", "/home/alok/Downloads/organizations-100.csv") \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .load()

    df.printSchema()

    df.select("Founded").distinct().show()

    filtered_df = df.select("Founded", "Country") \
        .where(col("Founded") > 1985)

    filtered_df.show()
    kv_rdd = filtered_df.rdd.map(lambda row: (row["Country"], 1))
    count_rdd = kv_rdd.reduceByKey(lambda v1, v2: v1 + v2)

    count_list = count_rdd.collect()
    for x in count_list:
        print(x)
