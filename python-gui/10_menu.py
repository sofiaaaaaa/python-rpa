import time
import tkinter.ttk as ttk
from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

def create_new_file():
    print("새파일 만들기")

# File
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴 
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu.add_cascade(label="Language", menu=menu_lang)

# 체크버튼  
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()
