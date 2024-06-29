from module.windows import *
from module.downloader_selenium import*


print("execute")
window=window()
path=window.chrome_driver_path
url=window.download_url
down_load_path=window.save_path
downloader_selenium(path,url,down_load_path)
    
    
    