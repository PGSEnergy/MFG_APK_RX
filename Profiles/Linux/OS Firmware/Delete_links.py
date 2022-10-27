import os
from shutil import copyfile
from pathlib import *

current_dir = Path.cwd()
path = str(current_dir) + "/files"
files = os.listdir(path=path)
counter = 0
flag = 0
link = []
file = []

exceptions = ["boot.scr","ea-image-base-imx6sxea-com.tar.bz2","imx6sxea-com-kit_v2-m4.dtb","M4ERPC.bin","SPL-imx6sxea-com","u-boot.img","zImage"]
print("Wait...\n")
for i in range(0,len(files)):
    path_to_file = path + "/" + files[i]
    if os.path.islink(path_to_file):
        link.append(path_to_file)
        file.append(os.path.realpath(path_to_file))

        counter += 1


for i in range(len(file)):
    copyfile(file[i],file[i]+str(i))

for i in range(len(file)):
    try:
        os.remove(file[i])
    except FileNotFoundError:
        print("Файла ",file[i]," нет\n")

for i in range(len(file)):
    os.rename(file[i]+str(i),link[i])

for i in range(len(files)):
    for a in range(len(exceptions)):
        if files[i] == exceptions[a]:
            flag = 1
            break
    if flag == 1:
        flag = 0
        continue
    if flag == 0:
        try:
            os.remove(path + "/" + files[i])
            print(files[i]," удалено","\n")
        except FileNotFoundError:
            print("Файла ", path + "/" + files[i], " нет\n")


print("\033[32m {}" .format("Done"))


# try:
#     os.rename(path + "/u-boot.img",path + "/u-boot-imx6sxea-com.img")
# except FileNotFoundError:
#     print("Файла u-boot.img нет")
