import time

for i in range(3):
    print('track')

    time.sleep(2)

# 多线程

import threading

print('start programme')


def takeANp():
    time.sleep(5)

    print('wake up')


# 注意传递函数，不是调用
threadObj = threading.Thread(target=takeANp)
threadObj.start()

print('end of program')
