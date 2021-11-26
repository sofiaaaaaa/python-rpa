from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

# 텍스트 위젯. 여러줄 입력가능
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요.")

# 한줄입력만 가능. 엔터키 입력 불가 
e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력하세요")


def btncmd():
    # 내용 출력 
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0: 0번째 컬럼 위치 
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END) 
    e.delete(0, END) 


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()


# s = "a b c d e f g"

# print(f's         : {s}')
