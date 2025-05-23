from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def transform_data(df):
    return df.withColumn("NewColumn", col("Age") * 2)


if __name__ == "__main__":
    spark = (SparkSession.builder
             .appName("ExampleApp")
             .getOrCreate())
    data = [(1, "alok", 21), (2, "aditya", 18), (3, "krishna", 20)]
    columns = ["ID", "Name", "Age"]
    df = spark.createDataFrame(data, columns)

    result_df = transform_data(df)
    result_df.show()

