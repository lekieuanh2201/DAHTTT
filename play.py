from playwright.sync_api import sync_playwright
import time
import ast
from facebook_scraper import get_posts
#beatvn.network 'datngobhlc@gmail.com' 'ygnZAE87'


def getpost_url( page_url, n):
    """
    input: url of public page (string)
           n = numberpost/15 (int)
           user(string)
           password(string)
    OUTPUT: (list) post_urls
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)

        context = browser.new_context(storage_state='state.json')
        
        page = context.new_page()

        page.goto('https://facebook.com')
        # page.fill('input#email', 'datngobhlc@gmail.com' )
        # page.fill('input#pass', 'ygnZAE87')
        # page.click('button[type=submit]')

        time.sleep(3)
        page.goto('https://touch.facebook.com/'+page_url)   
        time.sleep(1)
        for i in range(0,n):
            page.mouse.wheel(0,15000)
            time.sleep(2)
        posts_data = page.get_by_role('article').all()
        posts_url = []
        for post in posts_data:
            a = post.get_attribute('data-ft')
            try:
                post_dict = ast.literal_eval(a)
                post_id = post_dict['page_insights'][post_dict['actrs']]['targets'][0]['post_id']
                # print(post_id)
                post_url = 'https://www.facebook.com/'+ post_id
                posts_url.append(post_url)
            except:
                print('loi')
        storage = context.storage_state(path="state.json")
        return posts_url

x = getpost_url('beatvn.network', 2)
# # m nen thay bang acc dang dung tren may cua m, t chua co them tinh nang dang nhap bang cookie nen co hoi loi ty
print(x)
# posts = get_posts(post_urls=x)

# for post in posts:
#     print(post.keys())





    
    
        

    
    

