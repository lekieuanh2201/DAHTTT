from facebook_scraper import get_posts
from kafka import KafkaConsumer, KafkaProducer
import schedule

def kafka_get_text(kafka_producer: KafkaProducer, kafka_consumer: KafkaConsumer):
    cnt = 0
    for message in kafka_consumer:
        if cnt == 10:
            pass
        url = str(message.value)[2:-1]
        posts = get_posts(post_urls=[url])
        for post in posts:
            try:
                data = {
                    'url': post['original_request_url'],
                    'text': post['text'],
                    'time': post['time'],
                    'likes': post['likes'],
                    'comments': post['comments'],
                    'shares': post['shares'] 
                    }
                print('Starting sending data', data)
                kafka_producer.send(topic='topic_text_url', value=bytes(str(data), 'utf-8'))
                cnt += 1
            except:
                continue
            
if __name__ == "__main__":
    url_con = KafkaConsumer('topic_url_id', bootstrap_servers='localhost:9092')    
    
    producers = []
    for i in range(5):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producers.append(producer)

    for producer in producers:
        schedule.every(3).seconds.do(kafka_get_text, producer, url_con)
    while True:
        schedule.run_pending()
        