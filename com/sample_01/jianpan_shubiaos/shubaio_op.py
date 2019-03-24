import  pyautogui

# 获取鼠标当前位置
position = pyautogui.position()

print(position)

# 鼠标点击操作
pyautogui.click(100,150,button='right')
# pyautogui.click(100,150,button='left')
# 鼠标双击pyautogui.doubleClick()

# 鼠标拖动

# pyautogui.dragTo() 和 pyautogui.dragRel() 函