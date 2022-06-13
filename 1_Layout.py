import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * #__all__ *이라고 해도 __all__목록에 없으면 따로 import 해야함.
from tkinter import filedialog #파일다이얼로그는 위 목록에 없어서 새로 import
# import re

from PIL import Image


root = Tk()
root.title("그림 이어 붙이기")
# root.geometry("640x480") # 가로 * 세로
# root.geometry("640x480+500+300") # 가로 * 세로 + 출현위치(x좌표 + y좌표)


main_path = os.getcwd()

###################################################################
### Top frame 파일 추가, 선택 삭제
frame_top = Frame(root)
frame_top.pack(fill='x', padx=5, pady=5)

## 파일 추가, 선택 삭제 함수 def

########################이미지 파일을 선택하지 않았을 경우, 에러 메시지를 띄워보자.
def addfile() :
    files = filedialog.askopenfilenames(title='이미지 파일을 선택하세요.', \
        filetypes=(('PNG파일', '*.png'),('JPG 파일', '*.jpg'),('BMP 파일', '*.bmp'),('모든 파일', '*.*')), \
        initialdir=main_path)
    for file in files :
        if not file[-4:] == ".png" or file[-4:] == ".jpg" or file[-4:] == ".bmp" :
            msgbox.showerror("에러", "올바르지 않은 확장자 입니다.")
            return addfile() ## addfile 함수 재시작
    for i in files :
        listbox_file.insert(END, i)
    # print(files)
def delfile() :
    for i in reversed(listbox_file.curselection()) :
        listbox_file.delete(i)


## 파일 추가 버튼
btn_addfile = Button(frame_top, padx=5, pady=5, width=12, height=1, text='파일 추가', command=addfile)
btn_addfile.pack(side='left', padx=5, pady=5)
## 선택 삭제 버튼
btn_delfile = Button(frame_top, padx=5, pady=5, width=12, height=1, text='선택 삭제', command=delfile)
btn_delfile.pack(side='right', padx=5, pady=5)

###################################################################
### 2nd Frame listbox
frame_2nd = LabelFrame(root, text='선택된 파일 목록', borderwidth=0)
frame_2nd.pack(fill='x', padx=5, pady=5, ipadx=5, ipady=5)
## listbox & scrollbar
scrollbar_2nd = Scrollbar(frame_2nd)
scrollbar_2nd.pack(side='right', fill='y')
listbox_file = Listbox(frame_2nd, selectmode='extended', height=15, yscrollcommand=scrollbar_2nd.set)
listbox_file.pack(side='left', fill='both', expand=True)
scrollbar_2nd.config(command=listbox_file.yview)



###################################################################
### 3nd Frame save_path
frame_3rd = LabelFrame(root, text='저장 경로')#, borderwidth = 0)
frame_3rd.pack(fill='x', padx=5, pady=5, ipadx=5, ipady=5)

## save path 함수 def
def savepath() :
    directory = filedialog.askdirectory(title='저장할 폴더를 선택하세요.')
    if directory == '' : #사용자가 취소를 눌렀을 경우, return
        return
    entry_folder.config(state='normal')
    entry_folder.delete(0,END)
    entry_folder.insert(END, directory)
    entry_folder.config(state='readonly')
    

## Entry save path
entry_folder = Entry(frame_3rd, state='normal', readonlybackground=('white'))
entry_folder.insert(END, main_path)
entry_folder.config(state='readonly')
entry_folder.pack(side='left',fill='x', padx=5, pady=5, expand=True)

## Sellect folder button for save path
btn_savepath = Button(frame_3rd, text='폴더 선택', command=savepath, width=10)
btn_savepath.pack(side='right', padx=5, pady=5)



###################################################################
### 4nd Frame Combobox option
frame_4th = LabelFrame(root, text='선택 옵션')#, borderwidth = 0)
frame_4th.pack(fill='x', padx=5, pady=5, ipadx=5, ipady=5)

## Combobox 
# width opt
label_width = Label(frame_4th, text='가로 길이', width=10)
label_width.pack(side='left')
opt_width_values = ['원본 크기', 1024, 800, 640]
opt_width = ttk.Combobox(frame_4th, width=10, values=opt_width_values, state='readonly')
opt_width.current(0)
opt_width.pack(side='left', padx=5, pady=5)

# Interval opt
label_inter = Label(frame_4th, text='사진 간격', width=10)
label_inter.pack(side='left')
opt_inter_values = [0, 30, 60, 90]
opt_inter = ttk.Combobox(frame_4th, width=10, values=opt_inter_values, state='readonly')
opt_inter.current(0)
opt_inter.pack(side='left', padx=5, pady=5) 

# Save format opt
label_form = Label(frame_4th, text='파일 형식', width=10)
label_form.pack(side='left')
opt_form_values = ['png', 'jpg', 'bmp']
opt_form = ttk.Combobox(frame_4th, width=10, values=opt_form_values, state='readonly')
opt_form.current(0)
opt_form.pack(side='left', padx=5, pady=5) 



###################################################################
### Progress Bar
frame_5th = LabelFrame(root, text='진행도', borderwidth = 0)
frame_5th.pack(fill='x', padx=5, pady=5)


p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_5th, maximum=100, length=150, variable=p_var)
progressbar.pack(fill='x', padx=5, pady=5)



###################################################################
### Bottom frame
frame_bot = Frame(root)
frame_bot.pack(fill='both', expand=True)

##########################################저장할때 .png 자동으로 붙는 방법을 생각해 봅시다.
def start() :
    if listbox_file.size() == 0 :
        msgbox.showwarning("경고", "선택된 이미지 파일이 없습니다.\n이미지 파일을 추가해주세요.") #처음은 타이틀, 두번째는 내용
        return
    else :
        savename = filedialog.asksaveasfilename(title='저장할 이름을 작성해주세요.', filetypes=(('모든 파일', '*.*'),), initialdir=entry_folder.get())
        if savename == "" : return
        # print(savename)
        # print(listbox_file.get(0,END))
        images = [Image.open(i) for i in listbox_file.get(0,END)]


        ### 가로 크기를 변경하기 위한 옵션 처리
        opt_width_get = opt_width.get()
        if opt_width_get == "원본 크기" : opt_width_get = -1
        else : opt_width_get = int(opt_width_get)
        # 가로 크기에 맞춰 세로 크기 변경
        image_sizes = []
        if opt_width_get > -1 :
            image_sizes = [(opt_width_get, int(opt_width_get * i.size[1]/i.size[0])) for i in images]
        else :
            image_sizes = [(i.size[0], i.size[1]) for i in images]


        ##### 가로세로 크기 정보를 처리하는 방법 두 가지
        ## 1. 각 변수에 하나 씩 저장하는 방식
        # widths = [i.size[0] for i in images]
        # heights = [i.size[1] for i in images]
        ## 2. zip 함수를 이용하는 방식
        widths, heights = zip(*(image_sizes))


        # 생성될 사이즈 크기 확인 및 사진 생성
        max_widths = max(widths)
        sum_heights = sum(heights) + int(opt_inter.get())*(listbox_file.size()-1) # 사진 사이의 간격 만큼 최대 사이즈를 더해준다.
        result_img = Image.new("RGB", (max_widths,sum_heights),(255,255,255)) #배경 흰색


        # 사진 합치기
        y_offset = 0 # y 위치
        for idx, img in enumerate(images) : ## enumerate 함수를 이용해서 index값 뽑기
            img = img.resize(image_sizes[idx]) # 이미지를 가로크기에 맞춰 리사이즈
            result_img.paste(img, (0, y_offset)) # 리사이즈 된 img 파일을 붙여넣기
            y_offset += (img.size[1] + int(opt_inter.get())) # 다음에 붙여 넣을 y 위치 바꾸기

            progress = y_offset / sum_heights * 100
            p_var.set(progress)
            progressbar.update()

        result_img.save(savename+"."+opt_form.get())
        msgbox.showinfo("알림", "작업이 완료되었습니다.")

## 종료 버튼
btn_quit = Button(frame_bot, padx=5, pady=5, width=12, height=1, text='종료', command=root.quit)
btn_quit.pack(side='right', padx=5, pady=5)
## 시작 버튼
btn_start = Button(frame_bot, padx=5, pady=5, width=12, height=1, text='시작', command=start)
btn_start.pack(side='right', padx=5, pady=5)



root.resizable(False, False) # x 방향(가로) false, y 방향 false 크기 변경 방지
root.mainloop()
