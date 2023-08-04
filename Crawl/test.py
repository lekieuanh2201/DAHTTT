#667748092057481
from play import *
import pandas as pd
from facebook_scraper import get_posts

pagess = pd.read_csv('./Crawl/page_link_preprocess.csv')
pages = pagess['PageUrl']
for i in range(0, len(pages) ):
    print(str(i) +':' + pages[i])
    data = []
    try:
        for post in get_posts(
            #post_urls = ['813295533488554'],
            pages[i][25:],pages=2,
                        cookies = './Crawl/www.facebook.com_cookies.json',
                                options={
                                "progress": True,      
                                #"comments": 50,
                                "posts_per_page": 10,
                                }):
            print(post)
            timeslp = random.randint(20,40)
            time.sleep(timeslp)
            data.append([post['username'],post['post_id'], post['text'],post['timestamp'], post['likes'], post['comments']]) 
        df = pd.DataFrame(data)
        df.to_csv('post_data2.csv',header=False,mode="a", index=False)
        
    except:
        print('page Loi')
        time.sleep(900)


#crawlPostData('Crawl/mbasic.facebook.com_cookies1.json',38,100)