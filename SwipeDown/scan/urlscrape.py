import codecs
import re

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def scrape(count=1):
    driver.get("https://www.google.com/")
    search = driver.find_element(by=By.NAME, value='q')
    search.send_keys(re.compile('[A-Za-z0-9\-_]'))
    search.send_keys(Keys.ENTER)

    while count <= 100:
        for i in matches:
            file.write(str(count) + '.' + i + '\n')
            file.write(re.search('/[A-Za-z]+:\/\/[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_:%&;\?\#\/.=]+/g').split('\n'))
            file.write("The were " + str(len_match) + " matches found for your keyword:\n")
            file.close()
            count += 1
val = input("Enter a url: ")
wait = WebDriverWait(driver, 10)
driver.get(val)
get_url = driver.current_url
wait.until(EC.url_to_be(val))

if get_url == val:
    page_source = driver.page_source

soup = bs(page_source, features="html.parser")
keyword = input("Enter a keyword to find instances of in the article: ")
matches = soup.body.find_all(string=re.compile(keyword))
len_match = len(matches)
title = soup.title.text

file = codecs.open('scraping.txt', 'a+')


driver.quit()
