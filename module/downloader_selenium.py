#selenium
from module.windows import*
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import requests
import os




def downloader_selenium(driver_path,url,down_load_path):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    service=Service(driver_path)
    driver=webdriver.Chrome(service=service)


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

    #image_path=os.path.abspath("images2")
    image_path=down_load_path
    page=1
    for unit_src in all_src:
        img=requests.get(unit_src)
        f=open(image_path+"/"+f"img_{page}.jpg","wb")      #路徑要弄清楚，(open之後為欲建立檔案之總路徑(也要包含檔案格式)，不是存放地點)
        f.write(img.content)
        page+=1
    f.close()





