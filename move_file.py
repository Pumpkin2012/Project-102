import os
import shutil
from_dir="/Users/Aney/Downloads"
to_dir="/Users/Aney/Desktop/Coding/Project 102 - doument_files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    root,ext=os.path.splitext(file_name)
    print(root)
    print(ext)
    if ext=="empty":
        continue
    if ext in ['.txt','.doc','.docx','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir + '/' + "Document_Files"
        path3=to_dir + '/' + "Document_Files" + '/' + file_name
        if os.path.exists(path2):
            print("Moving "+file_name+".....")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving "+file_name+".....")
            shutil.move(path1,path3)