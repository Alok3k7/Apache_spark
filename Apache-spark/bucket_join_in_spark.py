from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Bucket Join Demo") \
        .master("local[*]") \
        .getOrCreate()

    orders_list = [("01", "02", 350, 1),
                   ("01", "04", 580, 1),
                   ("01", "07", 320, 2),
                   ("02", "03", 450, 1),
                   ("02", "06", 220, 1),
                   ("03", "01", 195, 1),
                   ("04", "09", 270, 3),
                   ("04", "08", 410, 2),
                   ("05", "02", 350, 1)]

    order_df = spark.createDataFrame(orders_list).toDF("order_id", "prod_id", "unit_price", "qty")

    product_list = [("01", "Scroll Mouse", 250),
                    ("02", "Optical Mouse", 350),
                    ("03", "Wireless Mouse", 450),
                    ("04", "Wireless Keyboard", 580),
                    ("05", "Standard Keyboard", 360),
                    ("06", "16 GB Flash Storage", 240),
                    ("07", "32 GB Flash Storage", 320),
                    ("08", "64 GB Flash Storage", 430)]

    product_df = spark.createDataFrame(product_list).toDF("prod_id", "prod_name", "list_price")

    order_df.write.bucketBy(3, "prod_id").saveAsTable("orders_bucketed")
    product_df.write.bucketBy(3, "prod_id").saveAsTable("products_bucketed")

    bucketed_order_df = spark.read.table("orders_bucketed")
    bucketed_product_df = spark.read.table("products_bucketed")

    bucket_join_df = bucketed_order_df.join(bucketed_product_df, "prod_id")

    bucket_join_df.show()

    spark.stop()
