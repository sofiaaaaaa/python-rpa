import time
import tkinter.ttk as ttk
from tkinter import * 
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

# btn1 = Button(root, text="버튼1", padx=10, pady=10)
btn1 = Button(root, text="버튼1", width=5, height=2)
btn2 = Button(root, text="버튼2", width=5, height=2) 
btn3 = Button(root, text="버튼2", width=5, height=2) 
btn4 = Button(root, text="버튼2", width=5, height=2) 

# btn1.pack(side="left")
# btn2.pack(side="right")
 # sticky 버튼 크기 늘리기 속성
btn1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn2.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn3.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn4.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn5 = Button(root, text="버튼1", width=5, height=2)
btn6 = Button(root, text="버튼2", width=5, height=2)
btn7 = Button(root, text="버튼2", width=5, height=2)
btn8 = Button(root, text="버튼2", width=5, height=2)

btn5.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn6.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn7.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn8.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn8 = Button(root, text="버튼1", width=5, height=2)
btn9 = Button(root, text="버튼2", width=5, height=2)
btn10 = Button(root, text="버튼2", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn8.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn9.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn10.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=2, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

btn_0 = Button(root, text="0", width=5, height=2)
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=3, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop()
