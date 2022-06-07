import os
def rename_dir(work_dir,old_ext,new_ext):
    # old_ext, new_ext = '.docx', '.txt'
    for file_name in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(file_name)
        file_ext = split_file[1] # 把所有文件属性（后缀）赋值给file_ext

        if old_ext == file_ext:
            new_file = split_file[0] + new_ext
            os.rename( #实现重命名操作
                        os.path.join(work_dir, file_name), #文件路径不变
                        os.path.join(work_dir, new_file)  # 文件后缀变为[new_ext]值
                        )


        print('完成重命名')
    print(os.listdir(work_dir))  # 打印修改后文件信息
    return

rename_dir('D:\\Users\\Desktop\\111', '.nc', '.txt')