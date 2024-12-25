import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import pickle as pk


class WEMAKESCHOLARS:
    data = {}
    opt = Options()

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def add_cookies(self):
        self.driver.get('https://www.wemakescholars.com/')
        self.driver.implicitly_wait(3)
        cookies = pk.load(open('cookies.pkl', 'rb'))
        for c in cookies:
            c['domain'] = '.wemakescholars.com'
            self.driver.add_cookie(c)

    def land_required_pages(self, page_url):
        self.driver.get(page_url)
        self.driver.implicitly_wait(5)

    def get_title(self):
        try:
            name = self.driver.find_element(By.XPATH, '//h1').text
            self.driver.implicitly_wait(5)
            self.data['Title'] = name
        except:
            self.data['Title'] = "N/A"

    def get_degree(self):
        try:
            degree = self.driver.find_element(By.XPATH, '//div[@class="col-sm-5"]/span').text
            self.driver.implicitly_wait(5)
            self.data['Degree'] = degree
        except:
            self.data['Degree'] = "N/A"

    def get_funding(self):
        try:
            funding = self.driver.find_element(By.XPATH, '(//div[@class="col-sm-7"]/div/span)[1]').text.split(', ')
            self.driver.implicitly_wait(4)
            self.data['Funding Type'] = funding[0]
            try:
                self.data['Funding Value'] = funding[1]
            except:
                self.data['Funding Value'] = "N/A"
        except:
            self.data['Funding Type'] = "N/A"
            self.data['Funding Value'] = "N/A"

    def get_provider(self):
        try:
            provider = self.driver.find_element(By.XPATH, '(//div[@class="col-sm-7"]/div/span)[2]').text
            self.driver.implicitly_wait(3)
            self.data['Scholarship Provider'] = provider
        except:
            self.data['Scholarship Provider'] = "N/A"

    def get_deadline(self):
        try:
            dead = self.driver.find_element(By.XPATH, '//div[@class="col-sm-5"]/div/span').text
            self.driver.implicitly_wait(3)
            self.data['Deadline'] = dead
        except:
            self.data['Deadline'] = 'N/A'

    def get_eligible_courses(self):
        try:
            eligiblecourse = self.driver.find_elements(By.XPATH, '//div[@class="text-line-div"]')
            self.driver.implicitly_wait(3)
            for e in eligiblecourse:
                if e.find_element(By.XPATH, './/p').text == 'Eligible Courses:':
                    ec = e.find_element(By.XPATH, './/span').text
                    self.driver.implicitly_wait(3)
                    self.data['Eligible Courses'] = ec
                    break
            else:
                self.data['Eligible Courses'] = "N/A"

        except:
            self.data['Eligible Courses'] = "N/A"


    def get_eligible_nationality(self):
        try:
            eligiblenat = self.driver.find_elements(By.XPATH, '//div[@class="text-line-div"]')
            self.driver.implicitly_wait(3)
            for e in eligiblenat:
                if e.find_element(By.XPATH, './/p').text == 'Eligible Nationalities:':
                    ec = e.find_element(By.XPATH, './/span').text
                    self.driver.implicitly_wait(3)
                    self.data['Eligible Nationalities'] = ec
                    break
            else:
                self.data['Eligible Nationalities'] = "N/A"

        except:
            self.data['Eligible Nationalities'] = "N/A"

    def get_scholarship_taker(self):
        try:
            scholartaker = self.driver.find_elements(By.XPATH, '//div[@class="text-line-div"]')
            self.driver.implicitly_wait(3)
            for e in scholartaker:
                if e.find_element(By.XPATH, './/p').text == 'Scholarship can be taken at:':
                    ec = e.find_element(By.XPATH, './/span').text
                    self.driver.implicitly_wait(3)
                    self.data['Scholarship Taker'] = ec
                    break
            else:
                self.data['Scholarship Taker'] = "N/A"

        except:
            self.data['Scholarship Taker'] = "N/A"

    def get_description(self):
        try:
            about = self.driver.find_element(By.XPATH, '//article[@class="more-about-scholarship"]/p').text
            self.driver.implicitly_wait(4)
            self.data['Description'] = about
        except:
            self.data['Description'] = "N/A"

    def get_criteria(self):
        try:
            eligibility_criteria = self.driver.find_element(By.XPATH, '//div[@class="editor"]/ul').text.replace('\n', ', ')
            self.driver.implicitly_wait(3)
            self.data['Eligibility Criteria'] = eligibility_criteria
        except:
            self.data['Eligibility Criteria'] = "N/A"

    def get_logo(self):
        try:
            logo = self.driver.find_element(By.XPATH, '//div[@class="col-md-2 col-sm-2 col-xs-6"]/a/img').get_attribute('src')
            self.driver.implicitly_wait(3)
            self.data['Logo'] = logo
        except:
            self.data['Logo'] = "N/A"

    def get_scholarship_url(self):
        try:
            s_url = self.driver.find_element(By.XPATH,'//a[@class="btn btn-new width100p font14 pull-right scholarship-applied"]').get_attribute('href')
            self.driver.implicitly_wait(3)
            self.data['Apply Now'] = s_url
        except:
            self.data['Apply Now'] = "N/A"

    def move_into_file(self, country, continent, dtype):
        self.data['Country'] = country
        self.data['Continent'] = continent
        self.data['Page Source'] = self.driver.current_url

        for key, value in self.data.items():
            print(key+": "+value)

        p = pd.DataFrame([self.data])
        p.to_csv("path", mode='a', header=not
                 os.path.exists("path"), index=False)
        p.to_csv("path", mode='a', header=not
        os.path.exists("path"), index=False)


country = str(input("Enter Country: ")).title()
continent = str(input("Enter Continent: ")).title()

bot = WEMAKESCHOLARS()
bot.add_cookies()
time.sleep(2)
my_list = ['Bachelors', 'Masters', 'Phd', 'Postdoc']
for l in my_list:
    with open(f"E:/FYPDS/Europe/UK/links/UK({l}).csv") as file:
        for f in file:
            bot.land_required_pages(f.strip())
            bot.get_title()
            bot.get_degree()
            bot.get_funding()
            bot.get_provider()
            bot.get_deadline()
            bot.get_eligible_courses()
            bot.get_eligible_nationality()
            bot.get_scholarship_taker()
            bot.get_description()
            bot.get_criteria()
            bot.get_logo()
            bot.get_scholarship_url()
            bot.move_into_file(country, continent, l)
