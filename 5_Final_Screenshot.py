import os
import time
import keyboard
from PIL import ImageGrab
from tkinter import *

def screenshot() :
    # YYYY년 MM월 DD일 HH시 MM분 SS초
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    # 현재 폴더 기준 저장 위치 지정
    curr_path = os.path.dirname(os.path.realpath(__file__))
    # 폴더가 없을 경우 폴더 생성 try/except
    img.save(f"{curr_path}/images/image{curr_time}.png")

def pressF9(window) :
    window.withdraw()
    screenshot()
    window.deiconify()

def screenshot_mode(root) :
    # root창 최소화
    root.withdraw()    
    window = trans_text(root)

    # 키보드 작동
    while True :
        if keyboard.is_pressed('f9') is True : pressF9(window)
        elif keyboard.is_pressed('esc') is True : break   

    # window 창 닫기
    window.destroy()
    # root창 복구
    root.deiconify()

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

def main() :
    root = Tk()
    root.title("F9 Screenshot, ESC quit")
    root.geometry("640x480") # 가로 * 세로

    # 매뉴 manu 
    # file, 시작, 저장되는 폴더 열기, 종료
    # option, 저장 경로 설정, 스샷모드 시작키, 스샷모드 종료키, 최소 스샷 간격
    # help, How to use, version


    # 시작 버튼
    sta_butt = Button(root, width=10, height=3, text="START", command=lambda : screenshot_mode(root))
    sta_butt.pack()

    # 종료 버튼
    quit_butt = Button(root, width=10, height=3, text="QUIT", command=root.quit)
    quit_butt.pack()

    root.resizable(False, False) # x 방향(가로) false, y 방향 false 크기 변경 방지
    root.mainloop()



if __name__ == "__main__" :
    main()