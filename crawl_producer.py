from kafka import KafkaProducer, KafkaConsumer
from Crawl.cookies_crawling import crawl_post
import pandas as pd
import json


def kafka_get_post(kafka_producer: KafkaProducer, pages, cookies):
    for page in pages:
        data = crawl_post(cookies, page, 1)
        # print(data)
        for js in data:
            kafka_producer.send(topic='fbpost', value=js)
            kafka_producer.flush()
        

def main():
    prod = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))


    pages = pd.read_csv('./Crawl/page_link_preprocess.csv')["PageUrl"]
    pages = pages[:100]
    # print("List of pages:", pages)
    kafka_get_post(prod, pages, './Crawl/www.facebook.com_cookies.json')

if __name__ == '__main__':
    main()
    
    
    

