import  os
import  shutil # 文件copy 模块

os.chdir('c:\\')

shutil.copy('f:\\ceshi\\test.txt','f:\\data') # 复制到了data 路径下

# 复制并且改名了
shutil.copy('f:\\ceshi\\test.txt','f:\\data\\test2.txt') # 复制到了data 路径下

# 文件和文件夹的移动与改名



