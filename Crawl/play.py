from playwright.sync_api import sync_playwright, Page
import time
import ast
from facebook_scraper import get_posts
#beatvn.network 'datngobhlc@gmail.com' 'ygnZAE87'
import pandas as pd
import random
import pyotp

def takePostData(list_post_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)

        context = browser.new_context(storage_state='state.json')
        page = context.new_page()
        for post_url in list_post_url:
            page.goto('https://facebook.com'+ post_url)

def getpost_url(n):
    """
    input: url of public page (string)
           n = numberpost/15 (int)
           user(string)
           password(string)
    OUTPUT: (list) post_urls
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(storage_state='state.json')
        
        page = context.new_page()

        page.goto('https://facebook.com')
        # page.fill('input#email', 'datngobhlc@gmail.com' )
        # page.fill('input#pass', 'ygnZAE87')
        # page.click('button[type=submit]')
        
        data = pd.read_csv('./Crawl/page_link_preprocess.csv')
        for i in range(0,len(data)):
            try:
                y = data['PageUrl'][i][25:]
                page.goto('https://touch.facebook.com/'+y)   

                for i in range(0,n):
                    page.mouse.wheel(0,15000)
                posts_data = page.get_by_role('article').all()
                posts_url = []
                for post in posts_data:
                    a = post.get_attribute('data-ft')
                    try:
                        post_dict = ast.literal_eval(a)
                        post_id = post_dict['page_insights'][post_dict['actrs']]['targets'][0]['post_id']
                        # print(post_id)
                        post_url = 'https://www.facebook.com/'+ post_id
                        print(post_url)
                        posts_url.append(post_id)
                    except:
                        print('loi')
                df = pd.DataFrame(posts_url)
                df.to_csv('./Crawl/post_urls.csv',header=False,index=False, mode="a")
            except:
                print('mang lag qua' + str(i))
        storage = context.storage_state(path="state.json")



"""
Sau khi chay duoc tam 100 post thi khong su dung duoc tool nay
Nguyen nhan: cookies nay da bi chan, khi lay qua nhieu bai trong 1 khoang thoi gian ngan la cut
             tool khong co tu dong cap nhat cookies
Giai phap:
    1. Dung crawl theo kieu selenium
    2. Chi dung cac public page??? Thu dung public xem dc bao nhieu page
"""
#MAX_COMMENTS = 30

mail1 = 'carlos1roncodadabg6635@hotmail.com'
pass1 = '8a8P7YdSRA1'
code1 = '2F6NLSJZ255DBDYUSSSHRI2Y2WJCUY7F'

mail2 = 'anajimenez83dadabg6635@hotmail.com'
pass2 = 'FHd9k2z6cXe'
code2 = '54LH7WSPT6HNAUNM7NBVHLVTNI4TY7KK'


def getCodeFrom2FA(code):
    totp = pyotp.TOTP(str(code).strip().replace(" ","")[:32])
    time.sleep(2)
    return totp.now()

def Login2Fa(email, password, code, page:Page):
    
    page.goto('https://facebook.com')
    page.fill('input#email', email )
    page.fill('input#pass', password)
    page.click('button[type=submit]')
#Xac nhan ma 2Fa
    page.fill('input[type=text]', getCodeFrom2FA(code))
    page.click('button[type=submit]')

    page.click('input[value=save_device]')
    page.click('button[type=submit]')

def CrawlPost(page:Page, postId):
    page.goto('https://facebook.com/'+str(postId))
    selector = page.query_selector('div.rq0escxv.l9j0dhe7.du4w35lb')
        # I save html code in variable to parse it by beautifulSoup
    print(selector)
    return selector

def main():
    with sync_playwright() as p:
#Dang nhap vao facebook
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        Login2Fa(mail2, pass2, code2, page)
        html = CrawlPost(page, 660408116111098)
        print(html)
        return html
main()

    
    
        

    
    

