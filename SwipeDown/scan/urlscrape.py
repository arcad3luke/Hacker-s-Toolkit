import codecs
import re

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
file.write(title + '\n')
file.write("The following are all instances of your keyword:\n")

def scrape(count=1):
    while count <= 100:
        for i in matches:
            file.write(str(count) + '.' + i + '\n')
            file.write(re.search('/[A-Za-z]+:\/\/[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_:%&;\?\#\/.=]+/g').split('\n'))
            file.write("The were " + str(len_match) + " matches found for your keyword:\n")
            file.close()
            count += 1
driver.quit()
