import  pyautogui

im = pyautogui.screenshot()

getpixel = im.getpixel((50, 200))

print(getpixel)

color = pyautogui.pixelMatchesColor(50, 200, (135, 147, 154))

print(color)


