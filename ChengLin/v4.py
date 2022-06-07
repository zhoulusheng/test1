#     name = os.path.splitext():分离文件名（name[0]和后缀name[1]）
#     os.rename(new_filename, old_filename)：修改文件名，若不在最初工作地址则需要更改
#     os.listdir(文件地址)：得到当前目录所有文件及文件夹（file）
#     os.path.join(根文件地址，file):得到file的绝对地址
#     os.path.isdir(file的绝对地址)：判断是否为文件夹（isfile判断是否为文件）
#     os.chdir(根文件地址)：修改根文件地址
#     os.getcwd():得到当前工作地址

import os
def renming(file):
    # """"修改后缀""""
    ext = os.path.splitext(file)          # 将文件名路径和后缀分开
    if ext[1] == '.txt':                  # 文件名：ext[0]
        new_name = ext[0] + '.html'       # 文件后缀：ext[1]
        os.rename(file, new_name)          # tree()已切换工作地址，直接替换后缀
    elif ext[1] == '.html':
        new_name = ext[0] + '.txt'
        os.rename(file, new_name)

def tree(path):
    # """递归函数"""
    file = os.listdir(path)                        # 获取当前目录的所有文件及文件夹
    for file in files:
        fiel_path = os.patn.join(path,file)        # 获取该文件的绝对路径
        if os.path.isdir(file_path):               # 判断是否为文件夹
            tree(fiel_path)                        # 开始递归
        else:
            os.chdir(path)                         # 修改工作地址（相当于文件指针到指定文件地址）
            renaming(file)


this_path = os.getcwd()          # 获取当前工作文件的绝对路径（文件夹）
tree(this_path)



