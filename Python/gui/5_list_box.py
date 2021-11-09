from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로세로 길이 

# height=0 : 모든 항목이 다보임 
listbox = Listbox(root, selectmode="extended", height=3)
listbox.insert(0, "솨과")
listbox.insert(0, "솨과3")
listbox.insert(0, "솨과2")
listbox.insert(0, "솨과1")
listbox.insert(END, "수박") # END 마지막에 insert
listbox.pack()

def btncmd():
    listbox.delete(0) # 맨 처음 항목 삭제 
    listbox.delete(END) # 맨 뒤의 항목 삭제

    # 갯수 확인 
    print("리스트에는", listbox.size(), "개가 있어요")  
    # pass

    # 항목 확인 
    print("1번째부터 3번째까지의 항목: ", listbox.get(0,2))

    # 선택된 항목 확인
    print("선택된 항목: ", listbox.curselection())
    

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
