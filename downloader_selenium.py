#selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import requests
import os

path="C:/Users/a2147/OneDrive/桌面/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service=Service(path)
driver=webdriver.Chrome(service=service)

url="https://nhentai.com/en/comic/orangemaru-ame-kakushitai-koto-the-idolm-at-ster-shiny-colors-digital/reader"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

down_load_path="C:/Users/a2147/OneDrive/桌面/miyabi/all"

driver.get(url)
sleep(5)
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


if not os.path.exists("images2"):
    os.mkdir("images2")  # 建立資料夾

image_path=os.path.abspath("images2")
page=1
for unit_src in all_src:
    img=requests.get(unit_src)
    f=open(image_path+"/"+f"img_{page}.jpg","wb")      #路徑要弄清楚，(open之後為欲建立檔案之總路徑(也要包含檔案格式)，不是存放地點)
    f.write(img.content)
    page+=1
f.close()





