export SPARK_HOME=/opt/spark-2.4.6
spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.8 spark_streaming_app.py



spark-submit --conf spark.pyspark.python=/usr/bin/python3.9 --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.8 spark-streaming-app.py


spark-submit --conf spark.pyspark.python=/usr/bin/python3.9 --packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.8 s-s-s.py


spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 sss.py

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.23.2 sss.py
