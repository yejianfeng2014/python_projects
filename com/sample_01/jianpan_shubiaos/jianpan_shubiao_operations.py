import  pyautogui

size = pyautogui.size()

print(size) #Size(width=1366, height=768)

# 移动鼠标
for i in range(10):

    pyautogui.moveTo(100,100,duration=0.25)
    pyautogui.moveTo(100,200,duration=0.25)
    pyautogui.moveTo(200,200,duration=0.25)
    pyautogui.moveTo(100,200,duration=0.25)


# pyautogui.moveRel() 函数 使用相对位置移动
print('开始使用相对位置移动')
for i in range(10):
    pyautogui.moveRel(100,0,duration=0.25)
    pyautogui.moveRel(0,100,duration=0.25)
    pyautogui.moveRel(-100,0,duration=0.25)
    pyautogui.moveRel(0,-100,duration=0.25)


