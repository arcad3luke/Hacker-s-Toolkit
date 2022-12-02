#!/bin/env/python3

import time
import bs4

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
soup = bs4.BeautifulSoup()

def scrape():
    dork = open('./GoogleHackMasterList.txt', 'r').readlines().pop()
    count = 0

    driver.get("https://www.google.com/")
    search = driver.find_element(by=By.NAME, value='q')
    result = search.send_keys()
    time.sleep(30)
    search.send_keys(Keys.ENTER)
    matches = soup.find_all(result)
    len_match = len(matches)
    count += 1
    time.sleep(300)
    driver.quit()

    with open('./scraping.txt', 'a+') as f:
        for i in matches:
            f.write(str(count) + '.' + i + '\n')
            f.write("There were " + str(len_match) + " matches found for your keyword:\n")
        f.close()
