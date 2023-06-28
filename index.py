# 引入 tkinter 模組
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from tkinter.ttk import Notebook
from tkinter import *
from PIL import  ImageTk, Image, ImageDraw
import sys
import rarfile
import unrar
import os
from tkinter import filedialog
execution_text="解壓縮"
files_path=[]
result=[]
subfolder=False

def execution():
    def unzip_path():
        path=[]
        for i in range(0,len(files_path)):
            path.append(files_path[i]) 
        return path
    def unzip(path,path2):
        for i in range(0,len(path)):
            rf =rarfile.RarFile(path[i]) #待解压文件
            rf.extractall(path2) #解压指定文件路径 
            rf.close()
    def unzip_subfolder(path):
        for i in range(0,len(path)):
            path2 = r"C:\Users\clove\Desktop\新增資料夾 (2)\{}".format(result[i])
            rf =rarfile.RarFile(path[i]) #待解压文件
            rf.extractall(path2) #解压指定文件路径 
        rf.close()
    
    path=unzip_path()
    if (subfolder==False):
        unzip_subfolder(path)
    else:
        path2 = r"C:\Users\clove\Desktop\新增資料夾 (2)"   
        unzip(path,path2)

    page1_but2['text']= 'Submitted'
    #print(path)
    
def show():
    global files_path
    global result
    files = filedialog.askopenfilenames()  # 點擊按鈕時選擇多個檔案
    print(files)                           # 以串列方式印出檔案路徑
    files_path=files
    for i in range(0,len(files_path)):
        listbox.insert(tk.END,files_path[i])
        basename = os.path.basename(files_path[i])
        result.append(os.path.splitext(basename)[0])
        print(result)
    

    
    
def exit():
    #tkinter.messagebox.showwarning(title="警告",message="ss")
    root.destroy()
    #root.quit()
    sys.exit(0)
        

# 建立主視窗 Frame
root = tk.Tk()

# 設定視窗標題
menu = tk.Menu(root)
menubar_1 = tk.Menu(menu)                        # 建立第一個選單的子選單，有三個選項
menubar_1.add_command(label="Open")              # 子選單第一個選項
menubar_1.add_command(label="Save")              # 子選單第二個選項
menubar_1.add_command(label="Exit")              # 子選單第三個選項
menubar_1.add_separator()
menubar_1.add_command(label="結束視窗",command=root.destroy)
menu.add_cascade(label='File', menu=menubar_1)   # 建立第一個選單 File，綁定子選單


menubar_2 = tk.Menu(menu)                        # 建立第二個選單的子選單，有三個選項
menubar_2.add_command(label="AAA")               # 子選單第一個選項
menubar_2.add_command(label="BBB")               # 子選單第一個選項
menubar_2.add_command(label="CCC")               # 子選單第一個選項
menubar_2.add_separator()                        # 子選單分隔線

menubar_2_more = tk.Menu(menubar_2)              # 建立子選單內的子選單，有三個選項
menubar_2_more.add_command(label="X")            # 子選單的子選單的第一個選項
menubar_2_more.add_command(label="Y")            # 子選單的子選單的第二個選項
menubar_2_more.add_command(label="Z")            # 子選單的子選單的第三個選項
menubar_2.add_cascade(label='File', menu=menubar_2_more)
menu.add_cascade(label='Test', menu=menubar_2)   # 建立第二個選單 File，綁定子選單
# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
root.geometry("600x400+250+150")
root.config(menu=menu)
root.title('批量工具')
tk_logo= ImageTk.PhotoImage(Image.open('icon_2.ico'))

#右鍵選單
def func():
    print('您通过弹出菜单执行了命令')
# 创建一个弹出菜单
menu = tk.Menu(root, tearoff=False)
menu.add_command(label="新建", command=func)
menu.add_command(label="複製", command=func)
menu.add_command(label="貼上", command=func)
menu.add_command(label="剪下", command=func)
# 定义事件函数
def command(event):
    # 使用 post()在指定的位置显示弹出菜单
    menu.post(event.x_root, event.y_root)
   
# 绑定鼠标右键，这是鼠标绑定事件
# <Button-3>表示点击鼠标的右键，1 表示左键，2表示点击中间的滑轮
root.bind("<Button-3>", command)







notebook=Notebook (root)
page1= Frame(root)
page2= Frame(root)
page3= Frame(root)
page4= Frame(root)
page5= Frame(root)
page6= Frame(root)
page7= Frame(root)
page8= Frame(root)

notebook.add (page1,text="解壓縮")
notebook.add (page2,text="加密壓縮")
notebook.add (page3,text="重新命名")
notebook.add (page4,text="移動檔案")
notebook.add (page5,text="文本檢查")
notebook.add (page6,text="暴力解碼")
notebook.add (page7,text="使用說明")
notebook.add (page8,text="關於")
notebook.pack (padx=10,pady=5,fill=tk.BOTH,expand=True)


#page 1
listbox=tk.Listbox(page1,width=60)
list1=Label(page1, text = "說明",font=('微軟正黑體',10))
list1.grid(row=1,column=0)
list1.logo = tk.Label(page1,height=64,width=64,bg ='gray94',fg='blue',image = tk_logo)  # 在 Lable 中放入圖片
list1.logo.grid(row=1,column=1,sticky='nw')
list2=Label(page1, text = "讀取路徑",font=('微軟正黑體',10,'bold'))
list2.grid(row=2)
listbox.grid(row=3,column=0)
page1_btn1 = tk.Button(page1,text='開啟檔案',font=('微軟正黑體',10,'bold'),command=show,padx=5, pady=5)
page1_btn1.grid(row=3,column=1,padx=5,pady=50)

output_text = tk.Label(page1, text='輸出路徑:')
output_text.grid(row=4, column=0,sticky='w')
output_link = tk.Entry(page1)
output_link.grid(row=4, column=0,padx=70,sticky='w')

page1_but2 = tk.Button(page1,text = execution_text,command = execution,font=('微軟正黑體',10,'bold'),padx=5, pady=5) # 按下按鈕所執行的函數
page1_but2.grid(row=10)






root.protocol("WM_DELETE_WINDOW",exit)
root.iconbitmap("icon.ico")

# 執行主程式
root.mainloop()
