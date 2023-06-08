from facebook_scraper import get_profile
from playwright.sync_api import sync_playwright
import time
import ast

def pagetiengviet(text):

    ans = True
    return ans

def searchPagebyKey(keyword):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)

        context = browser.new_context(storage_state='state.json')
        
        page = context.new_page()

        page.goto('https://facebook.com')
        time.sleep(3)
        page.goto('https://www.facebook.com/search/pages?q='+keyword)

        for i in range(0,10):
            page.mouse.wheel(0,15000)
            time.sleep(1)
        pages_infor = page.locator('xpath=/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]').all()
                                    
        file = open('page.txt')                                  
        for page_infor in pages_infor:
            page_url = page_infor.locator('xpath=/div[1]/div/div[1]/span/div/a').get_attribute('href')
            print(page_url)
            page_brief = page_infor.locator('xpath=/div[1]/div/div[2]/span/span').text_content().split('·')
            page_describe = page_infor.locator('xpath=div/div/div[3]/span/span').text_content()
            score = 0
            for infor in page_brief:
                try:
                    if ('người theo dõi' in infor):
                        x = infor.split(' n')[0]
                        if 'triệu' in x:
                            score = float(x.split('\xa0')[0].replace(' ','').replace(',','.'))*1000000
                        elif 'K' in x:
                            score = float(x.split('\xa0')[0][1:-1].replace(' ','').replace(',','.'))*1000
                    elif ('lượt thích' in infor):
                        x = infor.split(' l')[0]
                        if 'triệu' in x:
                            score = float(x.split('\xa0')[0].replace(' ','').replace(',','.'))*1000000
                        elif 'K' in x:
                            score = float(x.split('\xa0')[0][1:-1].replace(' ','').replace(',','.'))*1000
                except:
                    print(page_brief)

            if score > 100000:
                try:
                    if pagetiengviet(page_describe):
                        file.writelines(page_url)
                except:
                    print("page nay rac qua khonog co description")
        storage = context.storage_state(path="state.json")
    
searchPagebyKey('showbiz')