import os

source = "C:\\Users\\p_ant\\Documents\\test.txt"
dest = "C:\\Users\\p_ant\\Downloads\\text2.txt"


try:
    if os.path.exists(dest):
        print("There is already a file there")
    else:
        os.replace(source, dest)
        print(source + " Was moved")
except FileNotFoundError:
    print(source + "Was not found")