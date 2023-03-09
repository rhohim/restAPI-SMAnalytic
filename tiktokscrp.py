from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
from math import log, floor
from selenium.webdriver.common.by import By

def human_format(number):
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    magnitude = int(floor(log(number, k)))
    return '%.2f%s' % (number / k**magnitude, units[magnitude])

# op = webdriver.ChromeOptions()
# op.headless = True
# driver = webdriver.Chrome(options=op)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    'Chrome/80.0.3987.132 Safari/537.36'
# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--no-sandbox')
# chrome_option.add_argument('--disable-dev-shm-usage')
# chrome_option.add_argument('--ignore-certificate-errors')
# chrome_option.add_argument("--disable-blink-features=AutomationControlled")
# chrome_option.add_argument(f'user-agent={user_agent}')
# chrome_option.headless = True
driver = webdriver.Chrome()
driver.minimize_window()
data = {}
driver.get("https://www.tiktok.com/@cretivox")

time.sleep(1)
username = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h1').text
bio = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[2]').text
img_url = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/span/img').get_attribute("src")
print(img_url)
scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1
soup = BeautifulSoup(driver.page_source, "html.parser")
follow = soup.find_all("div", {"class": "tiktok-1kd69nj-DivNumber"})
follower = follow[0].strong.text
following = follow[1].strong.text
while True:
    # print(screen_height)
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # if (screen_height) * i > scroll_height:
    #     break 
    videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})
    
    # print(type(videos))
    # print(len(videos))
    if len(videos) >= 29 :
    
        break
total_like, total_comment, total_share = 0,0,0    
intcom, intlike, intshare = 0,0,0  
viewtik , datetik= [],[] 
for i in range(len(videos)):
    print(i)
    # print(len(videos))
    strview = str(videos[i].strong.text)
    value = strview.find('K')
    value2 = strview.find('M')
    print(strview)
    if (value != -1) or (value2 != -1):
        if value != -1 :
            strview = strview[:-1:]
            print(strview , i, " " , value, " in minus")
            intview = float(strview) * 1000
        elif value2 != -1 :
            strview = strview[:-1:]
            print(strview , i, " " , value, " in minus")
            intview = float(strview) * 1000000
                
    else:
        print(strview , i, " " , value, " positive")
        intview = int(strview)
    viewtik.append(int(intview))
    print(intview) #Total Views
    driver.get(videos[i].a["href"])
    like = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[1]/strong').text
    comment = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[2]/strong').text
    share = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/button[3]/strong').text
    
    
    
    like1 = like.find('K')
    like2 = like.find('M')
    comment1 = comment.find('K')
    comment2 = comment.find('M')
    share1 = share.find('K')
    share2 = share.find('M')
    
    if (like1 != -1) or (like2 != -1):
        if like1 != -1 :
            strview = like[:-1:]
            print(strview , i, " " , like1, " in minus")
            intlike = float(strview) * 1000
        elif like2 != -1 :
            strview = like[:-1:]
            print(strview , i, " " , like2, " in minus")
            intlike = float(strview) * 1000000
    else:
        print(strview , i, " " , like, " positive")
        intview = int(like)
            
    if (comment1 != -1) or (comment2 != -1):
        if comment1 != -1 :
            strview = comment[:-1:]
            print(strview , i, " " , comment1, " in minus")
            intcom = float(strview) * 1000
        elif comment2 != -1 :
            strview = comment[:-1:]
            print(strview , i, " " , comment2, " in minus")
            intcom = float(strview) * 1000000
    else:
        print(strview , i, " " , comment, " positive")
        intcom = int(comment)
            
    if (share1 != -1) or (share2 != -1):
        if share1 != -1 :
            strview = share[:-1:]
            print(strview , i, " " , share1, " in minus")
            intshare = float(strview) * 1000
        elif share2 != -1 :
            strview = share[:-1:]
            print(strview , i, " " , share2, " in minus")
            intshare = float(strview) * 1000000
    else:
        print(strview , i, " " , share, " positive")
        if share == "Share" or share == "":
            intshare = 0
        else:
            intshare = int(share)
    
    print(intlike, " ", intcom, " ",intshare)        
    
    total_like += int(intlike)
    total_comment += int(intcom) 
    total_share += int(intshare)
    
    
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    # timedate = soup.find("div", {"class": "tiktok-3axsrf-DivInfoContainer"})
    # print(videos[i].a["href"])
    # print(timedate)

    
    
    # try:
    #     span = timedate.find_all('span')
    #     # print(span[5].text)
    #     datetik.append(span[5].text)
    #     time.sleep(7)
    # except:
    #     datetik.append("video not found")
    # if i == 29 :
    #     break
    
#Show Output
print(viewtik)
print("View : " , human_format(np.sum(viewtik)))
print("Follower : ", following)
print("Following : ", follower)
print("Like : " , total_like)
print("comment : " , total_comment)
print("share : " , total_share)
print("username : " , username)
print("bio : " , bio)
driver.quit();
