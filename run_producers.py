import os
from threading import Thread
import crawl_producer
import crawl_producer1
 
prod = Thread(target=crawl_producer.main, daemon=True)
prod.start()
 
prod1 = Thread(target=crawl_producer1.main, daemon=True)
prod1.start()
