import pandas as pd
from facebook_scraper import get_posts
import random
import time
import os

def crawl_post(cookies_path, page, posts_per_page):
    data = []
    for post in get_posts(
            #post_urls = ['813295533488554'],
            page[25:],pages=2,
                        cookies = cookies_path,
                                options={
                                "progress": True,      
                                #"comments": 50,
                                "posts_per_page": posts_per_page,
                                }):
            # print(post)
            print(f"Crawling post...")
            timeslp = random.randint(20,40)
            time.sleep(timeslp)
            print(post['username'])
            data.append({"page": post['username'],
                        "post_id": post['post_id'], 
                        "text":post['text'],
                        "timestamp":post['timestamp'], 
                        "likes": post['likes'], 
                        "comments": post['comments']
                        }) 
            if len(data) > 3:
                  return data
#     df = pd.DataFrame(data)
    # df.to_csv('post_data2.csv',header=False,mode="a", index=False)
    return data

# pagess = pd.read_csv('./Crawl/page_link_preprocess.csv')
# pages = pagess['PageUrl']

# print(pages[1], crawl_post(pages[1], 2))

# for i in range(0, len(pages) ):
#     print(str(i) +':' + pages[i])
#     data = []
#     try:
#         for post in get_posts(
#             #post_urls = ['813295533488554'],
#             pages[i][25:],pages=2,
#                         cookies = './Crawl/www.facebook.com_cookies.json',
#                                 options={
#                                 "progress": True,      
#                                 #"comments": 50,
#                                 "posts_per_page": 10,
#                                 }):
#             print(post)
#             timeslp = random.randint(20,40)
#             time.sleep(timeslp)
#             data.append([post['username'],post['post_id'], post['text'],post['timestamp'], post['likes'], post['comments']]) 
#         df = pd.DataFrame(data)
#         df.to_csv('post_data2.csv',header=False,mode="a", index=False)
        
#     except:
#         print('page Loi')
#         time.sleep(900)


#crawlPostData('Crawl/mbasic.facebook.com_cookies1.json',38,100)