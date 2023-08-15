from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json
import os

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("ReadJSONFiles").getOrCreate()
es = Elasticsearch("http://localhost:9200")

def preprocess(txt: str)->str:
    # Code here
    
    ###########
    return txt

data_dir = 'C:/Users/dphamhuukhanh/Desktop/DAHTTT/data/'

# Reading data
df = None
for file in os.listdir(data_dir):
    f_path = os.path.join(data_dir, file)
    if df == None:
        df = spark.read.json(f_path)
    else:
        new_df = spark.read.json(f_path)
        df = df.union(new_df)

df.show()

# Preprocess data


#Insert data into Elastic Search
    # url_con = KafkaConsumer('topic_text_url', bootstrap_servers='localhost:9092')    
    
#     for messsage in url_con:
#         data_dict = messsage.value.decode('utf-8')
#         data_dict = data_dict.split(", '")
#         try:
#             data = {
#             'url': data_dict[0].split(": ")[1][1:-1],
#             'text': data_dict[1].split(": ")[1][1:-1],
#             'time': data_dict[2].split(": ")[1],
#             'likes': int(data_dict[3].split(": ")[1]),
#             'comments': int(data_dict[4].split(": ")[1]),
#             'shares': int(data_dict[5].split(": ")[1][:-1]) 
#             }
#             print(data)
#             es.index(index='posts', document=data)
#         except:
#             continue