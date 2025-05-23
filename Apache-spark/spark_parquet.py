from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[3]") \
        .appName("SparkSchemaDemo") \
        .getOrCreate()

    flightTimeParquetDF = spark.read \
        .format("parquet") \
        .option("path", "/home/alok/Downloads/flight-time.parquet") \
        .load()

    print("Num Partitions before: " + str(flightTimeParquetDF.rdd.getNumPartitions()))
    flightTimeParquetDF.groupBy("OP_CARRIER", "ORIGIN").count().show()

    partitionedDF = flightTimeParquetDF.repartition(5)
    print("Num Partitions after: " + str(partitionedDF.rdd.getNumPartitions()))
    partitionedDF.groupBy("OP_CARRIER", "ORIGIN").count().show()

    partitionedDF.write \
        .format("json") \
        .mode("overwrite") \
        .option("path", "json/") \
        .partitionBy("OP_CARRIER", "ORIGIN") \
        .option("maxRecordsPerFile", 10000) \
        .save()
