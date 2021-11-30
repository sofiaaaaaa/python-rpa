from PIL import ImageGrab
import time

# 5초 대기 
time.sleep(5) 

for i in range(1, 11): # 2초간격으로 10개 이미지 저장 
    img = ImageGrab.grab() # 현재 스크린 이미지 가져오기 
    img.save("image{}.png".format(i))
    time.sleep(2)

