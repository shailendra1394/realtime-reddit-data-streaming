# E2E Realtime Data Streaming Project

## Overview

This project implements an end-to-end (E2E) real-time data streaming solution using Apache Kafka, Apache Spark Structured Streaming, and Google BigQuery. The project involves data ingestion, stream processing, and data storage.

### 1. Data Ingestion:

- Utilized Apache Kafka for real-time data ingestion.
- Producers(reddit-to-kafka.py) publishes data to Kafka topic, and spark will consume these topic.

### 2. Stream Processing with Apache Spark Structured Streaming:

- Developed Apache Spark Structured Streaming pipelines in Python to perform real-time processing.

### 3. Data Storage:

- Leveraging the "pandas_gbq" library.
- Stored the processed data in a Google BigQuery table.

## Project Setup Instructions

Follow these steps to set up and run the Reddit-to-Kafka and Spark Streaming applications.

### Prerequisites:

- Python installed on your machine.
- Apache Kafka installed and running locally.
- Apache Spark installed and configured.
