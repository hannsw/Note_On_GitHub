import os,time
import pyautogui as pag
try:
    while True:
            print("Press Ctrl-C to end")
            x,y = pag.position() #返回鼠标的坐标
            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
            print(posStr)
            time.sleep(0.2)
            os.system('cls')#清除屏幕
except  KeyboardInterrupt:
    print('end....')