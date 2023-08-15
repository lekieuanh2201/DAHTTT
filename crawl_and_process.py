import pandas as pd
import pyspark
from Crawl.cookies_crawling import crawl_post
            
if __name__ == "__main__":
    pages = pd.read_csv('./Crawl/page_link_preprocess.csv')
    pages = pages[:50]
    for page in pages:
        # df = crawl_post(page, 2)
        # print(df)
        print(page)
        