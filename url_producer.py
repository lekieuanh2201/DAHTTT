from play import getpost_url
from facebook_scraper import get_posts
from kafka import KafkaProducer, KafkaConsumer
import schedule
import json

def kafka_get_post(kafka_producer: KafkaProducer, username, password, page_url, n):
    urls = getpost_url(username, password, page_url, n)
    # print(urls)
    for url in urls:
        kafka_producer.send(topic='topic_url_id', value=bytes(str(url), 'utf-8'))

if __name__ == '__main__':
    url_prod = KafkaProducer(bootstrap_servers='localhost:9092')
        
    print("Starting crawling...")
    schedule.every(20).seconds.do(kafka_get_post, url_prod, '','', 'beatvn.network', 2)
    
    while True:
        schedule.run_pending()
    
    
    

