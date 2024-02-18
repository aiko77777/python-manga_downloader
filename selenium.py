#selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import urllib.request
import os

path="C:/Users/a2147/OneDrive/桌面/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service=Service(path)
driver=webdriver.Chrome(service=service)

url="https://nhentai.com/en/comic/c90-the-seventh-sign-kagura-yuuto-magical-alisa-no-ichiban-hazukashii-yoru-the-legend-of-heroes-trails-of-cold-steel/reader"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

down_load_path="C:/Users/a2147/OneDrive/桌面/miyabi/all"

driver.get(url)
sleep(10)
driver.implicitly_wait(50)

source=driver.page_source
soup=BeautifulSoup(source,"html.parser")


all_src=[]

links=soup.find("main",class_="py-4")
links2=links.find_all("div",class_="vertical-image")
for links3 in links2:
    src=links3.find_all("img")
    for links4 in links3:
        all_src.append(links4["data-src"])
        print(links4["data-src"])


# if not os.path.exists("images"):
#     os.mkdir("images")  # 建立資料夾

# with open("images","wb") as f:
#     for unit_src in all_src:
#         driver.get(unit_src)
#         img=driver.page_source
#         f.write(img)




