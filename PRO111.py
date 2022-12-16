import os
import shutil

from_dir = "C:/Users/sudha/OneDrive/Documents/Python WHJ/Downloaded images/image_files"
to_dir = "C:/Users/sudha/Downloads"
listOfFiles = os.listdir(from_dir)
# print(listOfFiles)

for file_name in listOfFiles:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name 
        path2 = to_dir + '/' +"Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print("moving" + file_name + ".....")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("moving" + file_name + ".....")
            shutil.move(path1, path3)