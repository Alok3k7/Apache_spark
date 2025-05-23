import pytest
from pyspark.sql import SparkSession
from test_unit1 import transform_data


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.appName("test").getOrCreate()


def test_transform_data(spark):
    data = [(1, "saurabh", 30), (2, "abhishek", 25), (3, "Brijesh", 35)]
    columns = ["ID", "Name", "Age"]
    df = spark.createDataFrame(data, columns)

    transformed_df = transform_data(df)

    assert "NewColumn" in transformed_df.columns
    assert transformed_df.collect()[0]["NewColumn"] == 60
    assert transformed_df.collect()[1]["NewColumn"] == 50
    assert transformed_df.collect()[2]["NewColumn"] == 70



