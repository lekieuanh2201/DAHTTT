from facebook_scraper import get_posts

posts = get_posts( post_urls=['https://www.facebook.com/879869793499217', 'https://www.facebook.com/beatvn.network/posts/pfbid035aK2fANWo9oCrWzGQj6RjZ7oEpJbyuHYYo2dakTKHxXBAJEAqhdVsPBaPGHdLHesl?__cft__[0]=AZXpeno7-uw8HZ4G0cM4YZ55IVbNZ_Z3QIyo6ziDHzcRE-xJv8Ybcunvet25NNsrNFUm6XGBYVIhwF4OmopftxEAv98YY6ggOl2ipRpzz_rSSixGMzPYJ0l3T5wdJ4asNpjy0WtXIsk2lXT27Guh7raq&__tn__=%2CO%2CP-R'] )

for post in posts:
    print(post['text'])
