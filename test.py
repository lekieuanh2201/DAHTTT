from facebook_scraper import get_posts

posts = get_posts( post_urls=['https://www.facebook.com/879869793499217'] )

for post in posts:
    print(post['text'])
