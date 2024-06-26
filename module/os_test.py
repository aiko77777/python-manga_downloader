import os
if not os.path.exists("images"):
    os.mkdir("images")  # 建立資料夾

path=os.getcwd()    #取得工作目錄(該資料夾)
print(path)
print(os.path.abspath("images"))    #取得絕對路徑

