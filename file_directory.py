import os

path = "C:\\Users\\p_ant\\Documents\\new.txt"

if os.path.exists(path):
    print("that location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("That location doesn't exist")