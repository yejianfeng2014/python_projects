import os

join = os.path.join('user', 'bin', 'spame')


print(join)


# 当前工作目录

getcwd = os.getcwd()

print(getcwd)

# 切换工作目录

os.chdir('E:\python_projects')

os_getcwd = os.getcwd()

print(os_getcwd)



#os.makedirs()创建新文件夹

os.makedirs('C:\\delicious\\walnut\\waffles')

