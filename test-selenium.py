from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import pandas as pd
import numpy
from selenium.webdriver.common.by import By
from math import log, floor

# op = webdriver.ChromeOptions()
# op.headless = True
# driver = webdriver.Chrome(options=op)

def convert_str_to_number(x):
    total_stars = 0
    num_map = {'K':1000, 'M':1000000, 'B':1000000000}
    if x.isdigit():
        total_stars = int(x)
    else:
        if len(x) > 1:
            total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
    return int(total_stars)

def human_format(number):
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.2f%s' % (number / k**magnitude, units[magnitude])

driver = webdriver.Chrome()

data = {}

driver.get("https://www.youtube.com/@Tekotok/videos")

time.sleep(5)

# scroll_pause_time = 1
# screen_height = driver.execute_script("return window.screen.height;")
# i = 1

# # print(screen_height)
# driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
# i += 1
# time.sleep(scroll_pause_time)
# scroll_height = driver.execute_script("return document.body.scrollHeight;")  
# # if (screen_height) * i > scroll_height:
# #     break 

# soup = BeautifulSoup(driver.page_source, "html.parser")
# # print(soup)
# timedate = soup.find_all("div", {"class": "tiktok-lhxu2d-DivActionItemContainer"})
# follower = timedate[0].strong.text
# like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[1]/strong').text
# comment = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[2]/strong').text
# share = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[3]/strong').text
# print(like, comment, share)

link =  "link"
linkarr, viewarr, commentarr = [], [], []
subscriber = driver.find_element(By.XPATH, '//*[@id="subscriber-count"]').text
subscriber = subscriber.replace(" subscribers", "")

username = driver.find_element(By.XPATH, '//*[@id="text"]' ).text
lnks=driver.find_elements_by_tag_name("a")
print(len(lnks))
# traverse list
for lnk in lnks:
        # print(lnks[0])
        if "watch?v" in str(lnk.get_attribute('href')):
                # print(lnk.get_attribute('href'))
                if str(lnk.get_attribute('href')) != link:
                        link = lnk.get_attribute('href')
                        print(lnk.get_attribute('href'))
                        # driver.get(lnk.get_attribute('href'))
                        # time.sleep(5)
                        # view = driver.find_element(By.XPATH,'//*[@id="info"]/span[1]').text
                        # print(view)
                        # soup = BeautifulSoup(driver.page_source, "html.parser")
                        # viewdat = soup.find("div", {"class": "ytd-watch-metadata"})
                        # # span = viewdat.find_all('span')
                        # print(viewdat)
                        linkarr.append(lnk.get_attribute('href'))
                
for i in range(len(linkarr)):
        driver.get(linkarr[i])
        time.sleep(1)
        view = driver.find_element(By.XPATH,'//*[@id="info"]/span[1]').text
        view = view.replace(" views", "")
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # comment = driver.find_element_by_xpath('//*[@id="count"]/yt-formatted-string/span[1]').text
        viewarr.append(convert_str_to_number(view))
        # commentarr.append(comment)
        # print(comment)
print("total view " + str(len(linkarr)) + " videos : " + human_format(sum(viewarr)) )
print(username)
print(subscriber)
               
# driver.get(x)
# soup = BeautifulSoup(driver.page_source, "html.parser")
# view = driver.find_element(By.XPATH,'//*[@id="info"]/span[1]').text
# input_tag = soup.find_all(attrs={"label" : "simpleText"})
# # print(soup)
# # spanview = soup.find_all('span')
# print(view)



# def convert_str_to_number(x):
#     total_stars = 0
#     num_map = {'K':1000, 'M':1000000, 'B':1000000000}
#     if x.isdigit():
#         total_stars = int(x)
#     else:
#         if len(x) > 1:
#             total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
#     return int(total_stars)

# print(convert_str_to_number('537'))

