import os
def rename_dir(work_dir,old_ext,new_ext):
    # old_ext, new_ext = '.docx', '.txt'
    for file_name in os.listdir(work_dir):
        #
