import time
import tkinter.ttk as ttk
from tkinter import * 
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack(sid="right", fill="y") 

listbox = Listbox(frame, selectmode= "extended", height=10, yscrollcommand=scrollbar)
for i in range(1, 32):
    listbox.insert(END, str(i)+"일")

listbox.pack()
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)


root.mainloop()
