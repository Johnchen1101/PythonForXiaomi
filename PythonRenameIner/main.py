# IDE:python
# pyinstaller:./dist/main.exe
# how:放入根目录下
# do what:文件夹为A，多个子文件内容为1，2，3，
#             效果为:文件夹名字不动，子文件名字改为A_0000,A_0001






import os

path = './'      # 实际Path
# path = './test/'      # 测试Path
files = [i for i in os.listdir(path)]  # os.listdir返回指定目录下的所有文件和目录名
# print(files)
for file in files:
    pa = path + file  # 获得文件夹路径
    # print(pa)
    ff = [i for i in os.listdir(pa)]  # 获得当前文件夹下所有文件的名字
    # line = 0000
    # new_name = file + '_'
    # line = line + 1
    # os.rename(file ,file+"0000")
    # print(file)
    # print(ff)
    line = 0
    for ree in ff:
        ree = os.path.join(pa,ree)
        # print(ree)

        # print("befor:" + str(line))
        new_name = file+'_' + str(line).zfill(4)+".jpeg"
        os.rename(ree ,os.path.join(pa,new_name))
        line = line + 1
        # print("after:" + str(line))
    # print(path + '/' + file + '/' + 'metadata')