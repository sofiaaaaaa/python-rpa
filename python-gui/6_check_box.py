from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

chkvar = IntVar() # chkVar 에 int형으로 값을 저장함
chkbox = Checkbutton(root, text="오늘 하루만 보기", variable=chkvar)
chkbox.select() # 자동 선택 처리 
chkbox.deselect() # 선택처리 
chkbox.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제 
    print(chkvar2.get()) # 0 : 체크 해제 
    pass

chkvar2 = IntVar() # chkVar 에 int형으로 값을 저장함
chkbox2 = Checkbutton(root, text="일주일동안 보기", variable=chkvar2)
chkbox2.select() # 자동 선택 처리 
chkbox2.deselect() # 선택처리 
chkbox2.pack()

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
