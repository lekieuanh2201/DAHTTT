from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaPySparkElasticsearch") \
    .getOrCreate()

# Define the Kafka topic and bootstrap server
kafka_topic = "kafka-topic-1"
kafka_bootstrap_servers = "kafka:9092"

# Define the schema for the Kafka messages
message_schema = StructType([
    StructField("key", StringType(), nullable=False),
    StructField("value", StringType(), nullable=False)
])

# Read data from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# Convert the value column from binary to string
kafka_df = kafka_df.withColumn("value", kafka_df["value"].cast("string"))

# Parse the JSON message and extract key-value fields
parsed_df = kafka_df.select(from_json(col("value"), message_schema).alias("data")).select("data.*")

# Perform data transformation or analysis
# Example: Count occurrences of each key
key_counts = parsed_df.groupBy("key").count()

# Write the transformed data to Elasticsearch
es_host = "elasticsearch"
es_index = "my_es_index"

query = key_counts.writeStream \
    .outputMode("complete") \
    .format("org.elasticsearch.spark.sql") \
    .option("es.nodes", es_host) \
    .option("es.port", "9200") \
    .option("es.resource", es_index) \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .start()

query.awaitTermination()

