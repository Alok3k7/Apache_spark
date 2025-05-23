from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Shuffle Join Demo") \
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

    spark.conf.set("spark.sql.shuffle.partitions", 3)

    join_expr = order_df.order_id == product_df.prod_id
    join_df = order_df.join(product_df, join_expr, "inner")

    join_df.show()

    input("press a key to stop...")

