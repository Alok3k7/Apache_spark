from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

GCS_DATA_SOURCE_PATH = 'gs://source-data-for1/greenhouse-gas-emissions-industry-and-household-year-ended-2020.csv' # location of csv data file
GCS_DATA_OUTPUT_PATH = 'gs://output-data-for1/output_files' # output files saving location

def func_run():
  spark = SparkSession.builder.appName('hmda_app').getOrCreate()
  spark.sparkContext._jsc.hadoopConfiguration().set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")
  all_data = spark.read.csv(GCS_DATA_SOURCE_PATH, header=True)
  tf_df = all_data.withColumn("Total", lit("A"))
  tf_df.write.csv(GCS_DATA_OUTPUT_PATH, mode="overwrite", header=True)

if __name__ == "__main__":
    func_run()