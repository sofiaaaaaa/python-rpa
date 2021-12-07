import tkinter.ttk as ttk
from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정 


values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 숫자
readonly_combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택값 표시 
    pass

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
