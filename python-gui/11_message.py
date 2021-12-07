import time
import tkinter.ttk as ttk
from tkinter import * 
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

def info():
    msgbox.showinfo("알림", "정상적으로 예매되었습니다.")

def warn():
    msgbox.showwarning("경고", "매진되었습니다.")


def error():
    msgbox.showerror("오류", "매진되었습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "매진되었습니다.")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "매진되었습니다.")

def yesno():
    msgbox.askyesno("예 / 아니오", "매진되었습니다.")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="매진되었습니다.")
    print("응답ㅣ ", response)

    if response == 1:
        print("aaa")
    elif response == 0:
        print("bb")
    else: 
        print("cc")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="경고").pack()

Button(root, command=okcancel, text="확인취소").pack()
Button(root, command=retrycancel, text="재시도취소").pack()
Button(root, command=yesno, text="확인취소").pack()
Button(root, command=yesnocancel, text="예아니오취소").pack()

root.mainloop()
