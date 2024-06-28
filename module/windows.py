
from tkinter import*
from tkinter import filedialog
    
def call_windows():
    def direction():    #讓使用者新增下載的資料夾路徑並顯示
        save_path=filedialog.askdirectory()
        path.config(text=save_path)   #config可以直接改label的內容，不用再del 跟替換新的label
        path.place(x=100,y=200)
        
    def driver_dir():
        driver_path=filedialog.askdirectory()
        chrome_driver_path.config(text=driver_path)
        chrome_driver_path.place(x=100,y=50)

    
    
    window=Tk()
    window.geometry("900x500")
    window.title("manga downloader")
    window.config(background="#fff8dc")
    #window.iconbitmap("xx.ico")    #icon
    chrome_driver_path_button=Button(window,
                                     font=("Arial",20,"bold"),
                                     text="新增chromeDriver路徑",
                                     command=driver_dir)
    chrome_driver_path=Label(window,
                                   font=("Arial",15,"bold"),
                                   background="#fff8dc"
                                   )
    chrome_driver_path_label=Label(window,
                                   font=("Arial",20,"bold"),
                                   background="#fff8dc",
                                   text="chromeDriver路徑:")
    path=Label(window,
              font=("Arial",15,"bold"),
              background="#fff8dc"
              )    #new 一個label就好
    path_label=Label(window,
                     font=("Arial",20,"bold"),
                     background="#fff8dc",
                     text="下載路徑:")
    download_label=Label(window,
                         font=("Arial",20,"bold"),
                         background="#fff8dc",
                         text="下載連結:")
    direction_button=Button(window,
                            anchor=CENTER,
                            text="新增路徑",
                            font=("Arial",20,"bold"),
                            command=direction,
                            )
    download_button=Button(window,
                           text="下載",
                           font=("Arial",20,"bold"),
                           command=direction,
                           )
    entry_box=Entry(window,
                    font=("arial",14,"bold"),
                    width=60,
                    )
    chrome_driver_path_button.place(x=300,y=100)
    chrome_driver_path_label.place(x=100,y=10)
    path_label.place(x=100,y=150)
    download_label.place(x=100,y=300)
    direction_button.place(x=380,y=250)
    entry_box.place(x=100,y=350)
    download_button.place(x=400,y=400)
    # entry_box.pack()
    # download_button.pack()
    # direction_button.pack(side=BOTTOM)
    #direction_button.grid(column=5,row=5)
    window.mainloop()

call_windows()
