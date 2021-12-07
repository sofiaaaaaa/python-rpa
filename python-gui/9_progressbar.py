import time
import tkinter.ttk as ttk
from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 결정되지 않음. 언제 끝날지 모름 
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")  
# progressbar.start(10) # 10 ms 마다 움직임 
# progressbar.pack()



# def btncmd():
#     progressbar.stop() # 작동 중지 
#     pass

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 소수점표시 
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100 
        time.sleep(0.01) # 0.01초 대기 
        p_var2.set(i) 
        progressbar2.update() # ui 업데이트 


btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop()
