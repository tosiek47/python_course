import os
import shutil

path = "folder"

try:
    #os.remove(path) usuwanie plików
    #os.rmdir(path) #usuwanie folderów
    #shutil.rmtree(path) #usuwanie drzew plików (niebezpieczne)
except FileNotFoundError:
    print("This file was not found")
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("You can't delete that using that function")
else:
    print(path + " was deleted")
