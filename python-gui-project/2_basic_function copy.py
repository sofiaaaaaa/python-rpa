from tkinter import * 
import tkinter.ttk as ttk
from tkinter import filedialog # 서브 모듈은 __all__ 에 들어있지 않아서 별도로 명시해줘야함
import tkinter.messagebox as msgbox 

root = Tk()
root.title("Nado GUI")

# 파일 프레임 
file_frame = Frame(root)
file_frame.pack(padx=5, pady=5, fill="x")

# 파일 추가 
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")),
        initialdir="C:/"  # r"C:/Users..." r문자는 escape문자를 따로 쓰지 않게 해주는 옵션.
        )
    # 사용자가 선택한 파일 목록 출력 
    for file in files:
        print(file)
        list_file.insert(END, file)

# 파일 삭제 
def del_file():
    print(list_file.curselection())
    # reversed : 배열 요소 순서 반대로 반환 list(listObject) 는 list로 변환 
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None: # 사용자가 취소를 누를 때 
        return 
    print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 시작
def start():
    # 각 옵션 값을 확인 
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인 
    if list_file.size() == 0: 
        msgbox.showwarning("경고", "이미지파일을 추가하세요.")
        return 

    # 저장경로 확인
    if len(txt_dest_path.get()) == 0: 
        msgbox.showwarning("경고", "저장경로를 선택하세요.")
        return


btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(padx=5, pady=5,fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(padx=5, pady=5,fill="x", ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(padx=5, pady=5,side="right")


# 옵션 프레임 
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션 
lbl_width = Label(frame_option, text="가로넓이", width=3)
lbl_width.pack(padx=5, pady=5,side="left")

opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(padx=5, pady=5,side="left")

# 2. 간격 옵션
lbl_space = Label(frame_option, text="간격", width=3)
lbl_space.pack(padx=5, pady=5,side="left")

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(padx=5, pady=5,side="left")

# 3. 파일 포맷 옵션
lbl_format = Label(frame_option, text="포맷", width=3)
lbl_format.pack(padx=5, pady=5,side="left")

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(padx=5, pady=5,side="left")

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(padx=5, pady=5,fill="x", ipady=5)

p_bar = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_bar)
progress_bar.pack(padx=5, pady=5,fill="x")

# 실행 프레임 
frame_run = Frame(root)
frame_run.pack(padx=5, pady=5,fill="x", ipady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(padx=5, pady=5,side="right")

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(padx=5, pady=5,side="right")



root.resizable(False, False) # 윈도우 크기 고정 
root.mainloop()