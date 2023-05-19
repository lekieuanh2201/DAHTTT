from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json

es = Elasticsearch("http://localhost:9200")

if __name__ == "__main__":
    url_con = KafkaConsumer('topic_text_url', bootstrap_servers='localhost:9092')    
    
    for messsage in url_con:
        data_dict = messsage.value.decode('utf-8')
        data_dict = data_dict.split(", '")
        try:
            data = {
            'url': data_dict[0].split(": ")[1][1:-1],
            'text': data_dict[1].split(": ")[1][1:-1],
            'time': data_dict[2].split(": ")[1],
            'likes': int(data_dict[3].split(": ")[1]),
            'comments': int(data_dict[4].split(": ")[1]),
            'shares': int(data_dict[5].split(": ")[1][:-1]) 
            }
            print(data)
            es.index(index='posts', document=data)
        except:
            continue