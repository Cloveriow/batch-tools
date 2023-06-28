import tkinter as tk
from tkinter import filedialog
import rarafile

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

def show():
    files = filedialog.askopenfilenames()  # 點擊按鈕時選擇多個檔案
    print(files)                           # 以串列方式印出檔案路徑

btn = tk.Button(root,
                text='開啟檔案',
                font=('Arial',20,'bold'),
                command=show
                )
btn.pack()


root.mainloop()