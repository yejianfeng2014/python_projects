import pyautogui

screen = pyautogui.locateOnScreen('test3.png')

print(screen)  # 没有查找到


# Box(left=373, top=262, width=452, height=124)

# 选择图像的中心，然后单击鼠标

center = pyautogui.center(screen)

pyautogui.click(center,button='right')


