from PIL import ImageGrab
import time

time.sleep(5) # n초 대기. 프로그램 실행후 대기 시간

for i in range(1,11) :# 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()
    img.save(f"image{i}.png")
    time.sleep(2)
