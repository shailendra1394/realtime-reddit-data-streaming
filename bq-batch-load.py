from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from os import listdir
from os.path import isfile, join
from pandas_gbq import to_gbq

spark = SparkSession.builder.appName("BQBatchLoad").getOrCreate()

# Load date
date = '2024-01-03'

# BigQuery settings
project_id = "qwiklabs-gcp-03-96b39f52c439"
dataset_id = "my_dataset"
table_id = "reddit_world_news"

# Define the schema for the incoming JSON data
schema = StructType([
    StructField("title", StringType(), True),
    StructField("body", StringType(), True),
    StructField("author", StringType(), True),
    StructField("created_utc", DoubleType(), True)
])

csv_files_path = f'/home/student-04-7e89803ee339/spark_output/date={date}/'

csv_files = [f for f in listdir(csv_files_path) if isfile(join(csv_files_path, f)) and f.endswith('.csv')]

# Iterate over each CSV file and load into BigQuery
for csv_file in csv_files:
    full_path = join(csv_files_path, csv_file)
    df = spark.read.csv(full_path, header=False, schema=schema)
    df.printSchema()
    to_gbq(df.toPandas(), f"{project_id}.{dataset_id}.{table_id}", if_exists="append")