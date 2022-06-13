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
    img.save(f"{curr_path}/images/image{curr_time}.png")


def screenshot_mode() :
    keyboard.add_hotkey("F9", screenshot)
    keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행


def main() :
    root = Tk()
    root.title("F9 Screenshot, ESC quit")
    root.geometry("640x480") # 가로 * 세로

    sta_butt = Button(root, width=10, height=3, text="START", command=screenshot_mode)
    sta_butt.pack()

    quit_butt = Button(root, width=10, height=3, text="QUIT", command=root.quit)
    quit_butt.pack()

    root.resizable(False, False) # x 방향(가로) false, y 방향 false 크기 변경 방지
    root.mainloop()

if __name__ == "__main__" :
    main()