import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd

class WEMAKESCHOLARSLINKS:
    data = {}
    opt = Options()

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def land_required_pages(self, page_url):
        self.driver.get(page_url)
        self.driver.implicitly_wait(5)

    def get_links(self, dtype):
        links = self.driver.find_elements(By.XPATH, '//h2[@class="post-title"]/a')
        self.driver.implicitly_wait(3)
        for l in links:
            print("Link: "+l.get_attribute('href'))
            self.data['Links'] = l.get_attribute('href')
            p = pd.DataFrame([self.data])
            p.to_csv(f"path", mode='a', header=not
            os.path.exists(f"path"), index=False)

    def show_more(self):
        btn = self.driver.find_element(By.XPATH, '//input[@id="load-more"]')
        self.driver.implicitly_wait(3)
        btn.click()

    def handle_scrolling(self):
        scroll = self.driver.find_element(By.TAG_NAME, 'body')
        self.driver.implicitly_wait(3)
        for i in range(1, 16):
            scroll.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)



links = {
    "egypt": 'https://www.wemakescholars.com/scholarship?study=5&country=15',
    "south africs": 'https://www.wemakescholars.com/scholarship?study=5&country=45',
    "zambia": 'https://www.wemakescholars.com/scholarship?study=5&country=53'
}
bot = WEMAKESCHOLARSLINKS()
for i, j in links.items():
    bot.land_required_pages(j)
    time.sleep(30)
    bot.get_links(i)
