# # # 获取文件夹的名字
# # # 获取文件夹内的metadata文件夹名字
# # # 新名字后加：    _文件夹名字    #只命名metadata文件夹
#
import os
# import pandas as pd
import shutil
import zipfile

path = './'  # 实际Path
# path = './test/'      # 测试Path
files = [i for i in os.listdir(path)]  # os.listdir返回指定目录下的所有文件和目录名
# print(files)
# 创建压缩目录
# os.mkdir('./test/metadata')
os.mkdir('./metadata')

for file in files:
    pa = path + file  # 获得文件夹路径
    ff = [i for i in os.listdir(pa)]  # 获得当前文件夹下所有文件的名字
    for ree in ff:
        if ree == 'metadata':
            old_name = path + file + '/' + ree
            new = old_name + '_' + file
            aaa = ree + '_' + file
            os.rename(old_name, new)  # rename

            # 压缩文件
            source_path = './metadata/' + aaa
            output_filename = './metadata/' + aaa + '.zip'
            zip_file = zipfile.ZipFile(output_filename, 'w')
            pre_len = len(os.path.dirname(source_path))
            for parent, dirnames, filenames in os.walk(source_path):
                for filename in filenames:
                    print(f'{filename}')
                    path_file = os.path.join(parent, filename)
                    arcname = path_file[pre_len:].strip(os.path.sep)
                    zip_file.write(path_file, arcname)

            zip_file.close()

            # 压缩文件
            source_path = './metadata/' + aaa
            output_filename = './metadata/' + aaa + '.zip'
            zip_file = zipfile.ZipFile(output_filename, 'w')
            pre_len = len(os.path.dirname(source_path))
            for parent, dirnames, filenames in os.walk(source_path):
                for filename in filenames:
                    print(f'{filename}')
                    path_file = os.path.join(parent, filename)
                    arcname = path_file[pre_len:].strip(os.path.sep)
                    zip_file.write(path_file, arcname)

            zip_file.close()