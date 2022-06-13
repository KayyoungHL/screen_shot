import os
import sys
import time
import keyboard
from PIL import ImageGrab
from tkinter import *
from tkinter import filedialog


## save path 함수 def
def savepath(entry_path) :
    directory = filedialog.askdirectory(title='Select save folder')
    if directory == '' : #사용자가 취소를 눌렀을 경우, return
        return
    entry_path.config(state='normal')
    entry_path.delete(0,END)
    entry_path.insert(END, directory)
    entry_path.config(state='readonly')

def screenshot(dir, name) :
    # YYYY년 MM월 DD일 HH시 MM분 SS초
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()

    # 폴더가 없을 경우 폴더 생성 try/except
    try :
        img.save(dir+f"/{name}_{curr_time}.png")
    except :
        # print("폴더가 없어서 폴더를 생성 후 저장")
        os.makedirs(dir)
        img.save(dir+f"/{name}_{curr_time}.png")

def trans_text (root) :
    window = Toplevel(root)
    window.wm_attributes("-topmost", 1) # 항상 위
    window.wm_attributes('-transparentcolor', '#abcdef') # 특정 색을 투명색으로 정의
    window.config(bg='#abcdef') # 정해진 색을 이용해 투명 배경
    window.geometry('400x200+0+0')
    label1 = Label(window, text="F9 Screenshot, ESC quit", fg="red", bg="black", font=("Times New Roman",20,"bold"), relief="solid")
    label1.pack(side='left', anchor=NW)

    window.overrideredirect(True) # 창 프레임 제거
    window.update()

    return window # 윈도우 값 리턴

def screenshot_mode(root, dir, name="Image", sm_start="f9", sm_quit="esc") :
    # root창 최소화
    root.withdraw()    
    window = trans_text(root)

    # 키보드 작동
    while True :
        if keyboard.is_pressed(sm_start) is True :
            window.withdraw()
            screenshot(dir, name)
            window.deiconify()
        elif keyboard.is_pressed(sm_quit) is True : break   

    # window 창 닫기
    window.destroy()
    # root창 복구
    root.deiconify()

def main() :
    root = Tk()
    root.title("F9 Screenshot, ESC quit")
    # root.geometry("600x400") # 가로 * 세로
    if getattr(sys, 'frozen', False):
        #test.exe로 실행한 경우,test.exe를 보관한 디렉토리의 full path를 취득
        curr_path = os.path.dirname(os.path.abspath(sys.executable))
    else:
        #python test.py로 실행한 경우,test.py를 보관한 디렉토리의 full path를 취득
        curr_path = os.path.dirname(os.path.abspath(__file__))
    # curr_path = os.path.dirname(os.path.realpath(__file__))
    # curr_time = time.strftime("_%Y%m%d_%H%M%S")
    dir = f"{curr_path}/images" # dir - default
    name = "Image" # name - default

    # str_command = screenshot_mode(root, dir=dir) ## 옵션 추가 할 예정
    # osf_command = os.startfile(dir)

    ###################################################################
    # 매뉴 manu 
    menu = Menu(root)
    # files, 시작, 저장되는 폴더 열기, 종료
    menu_file = Menu(menu, tearoff=0)
    menu_file.add_command(label="Start", command = lambda : screenshot_mode(root, dir=dir, name=entry_name.get()))
    menu_file.add_command(label="Open Save Folder", command = lambda : os.startfile(dir))
    menu_file.add_separator()
    menu_file.add_command(label="Exit", command=root.quit)
    menu.add_cascade(label="File", menu=menu_file)

    # option, 저장 경로 설정, 스샷모드 시작키, 스샷모드 종료키, 최소 스샷 간격
    menu_opt = Menu(menu, tearoff=0)
    menu_opt.add_command(label="Save Path", command = lambda : savepath(entry_path))
    menu_opt.add_separator()
    # menu_opt.add_command(label="Screenshot_mode_start_KEY", command="")
    # menu_opt.add_command(label="Screenshot_mode_quit_KEY", command="")
    # menu_opt.add_separator()
    # menu_opt.add_command(label="Time Interval", command="")
    menu.add_cascade(label="Option", menu=menu_opt)


    # help, How to use, version
    # menu_help = Menu(menu, tearoff=0)
    # menu_help.add_command(label="How to use",command = lambda : howtouse(root))
    # menu_help.add_command(label="Version", command="")
    # menu.add_cascade(label="Help", menu=menu_help)

    root.config(menu=menu)

    ###################################################################
    ### Frame save_name
    save_name_frame = LabelFrame(root, text="Save Name")
    save_name_frame.pack(fill='x', padx=5, pady=5, ipadx=5, ipady=5)

    ## Entry save name
    entry_name = Entry(save_name_frame, state='normal', readonlybackground=('white'), justify="right")
    entry_name.insert(END, name)
    entry_name.pack(side='left',fill='x', padx=5, pady=5, expand=True)
    

    ## label +alpha
    label_name = Label(save_name_frame, text=f"_YYYYMMDD_HHMMSS.png")
    label_name.pack(side='left')

    ###################################################################
    ### Frame save_path
    save_path_frame = LabelFrame(root, text='Save Path')#, borderwidth = 0)
    save_path_frame.pack(fill='x', padx=5, pady=5, ipadx=5, ipady=5)

    ## Entry save path
    entry_path = Entry(save_path_frame, state='normal', readonlybackground=('white'), width=50)
    entry_path.insert(END, dir)
    entry_path.config(state='readonly')
    entry_path.pack(side='left', padx=5, pady=5, expand=True)

    ## Sellect folder button for save path
    savepath_butt = Button(save_path_frame, width=10, height=3, text='Folder select', command = lambda : savepath(entry_path))
    savepath_butt.pack(side='right', padx=5, pady=5)


    ###################################################################
    ### Frame button
    #
    button_frame = Frame(root)#, borderwidth = 0)
    button_frame.pack(fill='x', padx=5, pady=5, ipadx=5, ipady=5)     
    # 시작 버튼
    sta_butt = Button(button_frame, width=10, height=3, text="START", command=lambda : screenshot_mode(root, dir=dir, name=entry_name.get()))
    sta_butt.pack(side=LEFT, padx=5, pady=5)


    # 저장 폴더 오픈 버튼
    osf_butt = Button(button_frame,  width=10, height=3, text="Open\nSaved\nFolder", command = lambda : os.startfile(dir))
    osf_butt.pack(side=LEFT, padx=5, pady=5)


    # 종료 버튼
    quit_butt = Button(button_frame, width=10, height=3, text="QUIT", command=root.quit)
    quit_butt.pack(side=RIGHT, padx=5, pady=5)

 
    root.resizable(False, False) # x 방향(가로) false, y 방향 false 크기 변경 방지
    root.mainloop()



if __name__ == "__main__" :
    main()