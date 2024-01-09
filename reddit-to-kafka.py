# importing the necessary libraries
import praw
from kafka import KafkaProducer
import json
import configparser
from prawcore.exceptions import Redirect

# reading config file
config=configparser.ConfigParser()
config.read_file(open('reddit.config'))

# reddit API credentials
client_id = config.get('REDDIT','my_client_id')
client_secret = config.get('REDDIT','my_client_secret')
username = config.get('REDDIT','my_reddit_username')
password = config.get('REDDIT','my_reddit_password')
user_agent = config.get('REDDIT','my_user_agent')

# kafka settings
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'reddit-topic'

# creating a reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# creating a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# streaming Reddit data and publishing to Kafka
try:
    subreddit = reddit.subreddit('worldnews')  # Replace 'my_subreddit' with the subreddit you're interested in

    for submission in subreddit.stream.submissions():
        message = {
            'title': submission.title,
            'body': submission.selftext,
            'author': submission.author.name,
            'created_utc': submission.created_utc
        }
        producer.send(kafka_topic, value=message)

except Redirect as e:
    # Handle the Redirect exception
    print(f"Redirect exception: {e}")
