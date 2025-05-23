from pyspark.sql import SparkSession
from pyspark.sql import functions as f

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Agg Demo") \
        .master("local[2]") \
        .getOrCreate()

    invoice_df = spark.read \
        .format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("data/invoices.csv")

    invoice_df.select(f.count("*").alias("Count *"),
                      f.sum("Quantity").alias("TotalQuantity"),
                      f.avg("UnitPrice").alias("AvgPrice"),
                      f.countDistinct("InvoiceNo").alias("CountDistinct")
                      ).show()

    invoice_df.selectExpr(
        "count(1) as `count 1`",
        "count(StockCode) as `count field`",
        "sum(Quantity) as TotalQuantity",
        "avg(UnitPrice) as AvgPrice"
    ).show()

    summary_df = invoice_df \
        .groupBy("Country") \
        .agg(
        f.sum("Quantity").alias("TotalQuantity"),
        f.round(f.sum(f.expr("Quantity * UnitPrice")), 2).alias("InvoiceValue"),
        f.expr("round(sum(Quantity * UnitPrice),2) as InvoiceValueExpr")
    )

    summary_df.show()
