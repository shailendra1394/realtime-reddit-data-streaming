# E2E realtime-reddit-data-streaming
This project streams data from Reddit using python PRAW library, publishes it to Kafka, and processes it in real-time with Spark Structured Streaming.

# Overview
This project implements an end-to-end (E2E) real-time data streaming solution using Apache Kafka, Apache Spark Structured Streaming, and Google BigQuery. The project involves data ingestion, stream processing, and data storage.

## 1. Data Ingestion:
Utilize Apache Kafka for real-time data ingestion.
Producers publish data to Kafka topics, and Beam will consume these topics.

## 2. Stream Processing with Apache Spark Structured Streaming:
Developed Apache Spark Structured Streaming pipelines in Python to perform real-time processing.

## 3. Data Storage:
Leveraging the "pandas_gbq" library.
Store the processed data in Google BigQuery.

# Project Setup Instructions
Follow these steps to set up and run the Reddit-to-Kafka and Spark Streaming applications.

## Prerequisites:
Python installed with required dependencies on your machine.
Apache Kafka installed and running locally.
Apache Spark installed and configured.
