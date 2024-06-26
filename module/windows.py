
from tkinter import*
from tkinter import filedialog
    
def call_windows():
    def direction():    #讓使用者新增下載的資料夾路徑並顯示
        save_path=filedialog.askdirectory()
        path_label.config(text=save_path)   #config可以直接改label的內容，不用再del 跟替換新的label
        path_label.pack()
        
        
    
    
    window=Tk()
    window.geometry("900x500")
    window.title("manga downloader")
    window.config(background="#fff8dc")
    #window.iconbitmap("xx.ico")    #icon
    path_label=Label(window,
                     font=("Arial",20,"bold"))    #new 一個label就好
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
    entry_box.pack()
    download_button.pack()
    direction_button.pack(side=RIGHT)
    #direction_button.grid(column=5,row=5)
    window.mainloop()

call_windows()
