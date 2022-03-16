import os 
import shutil
# os.system("date")
# os.mkdir("/mansiprojects/newfolder")
path=input("enter the name of directory to be sorted: ")
listOfFiles=os.listdir(path)
# print("listOfFiles")
# print(listOfFiles)
for file in listOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)


