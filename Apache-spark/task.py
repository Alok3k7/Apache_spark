from pyspark.sql.functions import regexp_replace, split
from pyspark.sql.types import IntegerType, Row
import json

if __name__ == "__main__":
    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("hello") \
        .master("local[3]") \
        .getOrCreate()

    data_list = [
        (1, "Aarav", 25, "M", "123 Street, City1", "123-456", "$1,000"),
        (2, "Aanya", 30, "F", "456 Avenue, City2", "789-012", "$1,500"),
        (3, "Advait", 28, "M", "789 Road, City3", "345-678", "$2,000"),
        (4, "Aisha", 22, "F", "987 Lane, City4", "901-234", "$1,200"),
        (5, "Arjun", 29, "M", "654 Lane, City5", "567-890", "$1,800"),
        (7, "Diya", 27, "F", "321 Road, City6", "234-567", "$900"),
        (8, "Ishaan", 34, "M", "876 Avenue, City7", "876-543", "$3,000"),
        (9, "Kavya", 25, "F", "543 Street, City8", "345-678", "$2,500"),
        (10, "Reyansh", 23, "M", "210 Road, City9", "987-654", "$1,800"),
        (11, "Saanvi", 31, "F", "789 Lane, City10", "654-321", "$1,200"),
        (12, "Kabir", 35, "M", "345 Alley, City11", "567-890", "$1,800"),
        (13, "Sara", 28, "F", "876 Crescent, City12", "123-456", "$2,200"),
        (14, "Rohan", 32, "M", "543 Park, City13", "789-012", "$1,300"),
        (15, "Aaliyah", 26, "F", "210 Square, City14", "345-678", "$2,00,00,00,333"),

    ]

    df = spark.createDataFrame(data_list).toDF("Index no.", "Name", "Age", "Gender", "Address", "Pincode", "Amount")

    df_cleaned_pincode = df.withColumn("PinCode", regexp_replace("PinCode", "-", "").cast(IntegerType()))
    df_cleaned_amount = df.withColumn("Amount", regexp_replace("Amount", "[$,]", "").cast(IntegerType()))

    df_split_address = df_cleaned_amount.withColumn("AddressSplit", split("Address", ","))
    df_split_address = df_split_address.withColumn("Street", df_split_address["AddressSplit"].getItem(0))
    df_split_address = df_split_address.withColumn("City", df_split_address["AddressSplit"].getItem(1))
    df_split_address = df_split_address.drop("AddressSplit")

first_row = df_split_address.first()
data_in_row = first_row.asDict()
print(data_in_row)


