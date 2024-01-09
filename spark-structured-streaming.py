from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, from_unixtime
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = SparkSession.builder.appName("StructuredKafkaRedditStream").getOrCreate()

# Define the schema for the incoming JSON data
schema = StructType([
    StructField("title", StringType(), True),
    StructField("body", StringType(), True),
    StructField("author", StringType(), True),
    StructField("created_utc", DoubleType(), True)
])
# Read from Kafka topic
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "reddit-topic") \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON data and select relevant columns
parsed_df = kafka_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Extract date from created_utc and convert it to a string format
parsed_df = parsed_df.withColumn("date", from_unixtime("created_utc").cast("date"))

#Write data to CSV files with partitioning by date
output_path = "/home/student-04-56c483706573/spark_output"
checkpoint_path = "/home/student-04-56c483706573/spark_checkpoint"

query = parsed_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", output_path) \
    .option("checkpointLocation", checkpoint_path) \
    .partitionBy("date") \
    .start()

query.awaitTermination()