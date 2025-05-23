from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("hello") \
        .master("local[3]") \
        .getOrCreate()

    data_list = [("alok", 20, "m"),
                 ("niharika", 52, "f"),
                 ("yogesh", 21, "m"),
                 ("harshal", 21, "m")]

    df = spark.createDataFrame(data_list).toDF("Name", "Age", "gender")
    df.show()

