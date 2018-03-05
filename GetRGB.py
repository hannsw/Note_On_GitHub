import pyautogui

im = pyautogui.screenshot()

print(im.getpixel((433, 942)))
