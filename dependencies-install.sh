#-----------------------------Kafka Install
sudo apt -y update

# Install OpenJDK 11
sudo apt -y install openjdk-11-jdk

# Download the latest version of Kafka
wget https://downloads.apache.org/kafka/3.6.0/kafka_2.12-3.6.0.tgz

# Extract Kafka
tar -xzf kafka_2.12-3.6.0.tgz

#-----------------------------Spark Install
# Download the latest Apache Spark (replace with the latest version)
wget https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz

# Extract the downloaded tarball
tar -xvf spark-3.2.0-bin-hadoop3.2.tgz

# Move Spark to a desired location (for example, /opt)
sudo mv spark-3.2.0-bin-hadoop3.2 /opt/spark-3.2.0

# Create a symbolic link to make it easier to reference
sudo ln -s /opt/spark-3.2.0 /opt/spark

# Add Spark binaries to the PATH
echo 'export PATH=$PATH:/opt/spark/bin' >> ~/.bashrc
source ~/.bashrc

export SPARK_HOME=/opt/spark

#-----------------------------python dependencies
sudo apt -y install pip
pip3 install kafka-python
pip3 install praw
pip3 install pyspark==3.2.0