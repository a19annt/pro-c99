import time
import os
import shutil

def remove_file(path):
    if not os.remove(path):
        print('path is removed successfully')
    else:
        print('unable to delete path')

def remove_folder(path):
    if not shutill.rmtree(path):
        print('path is removed successfully')
    else:
        print('unable to delete path')
def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

deletedFolders=0
deletedFiles=0
path=input("Enter the path: ")
days=int(input("Enter the days: "))

seconds=time.time()-(days*24*60*60)

if (os.path.exists(path)):
    for route_folders,folders,files in os.walk(path):
        if seconds>=get_file_or_folder_age(route_folders):
            remove_folder(route_folders)
            deletedFolders+=1
            break
        else:
            for folder in folders:
                folder_path=os.path.join(route_folders,folders)
                if seconds>=get_file_or_folder_age(folder_path):
                    remove_folder(folder_path)
                    deletedFolders+=1
            for file in files:
                file_path=os.path.join(route_folders,file)
                if seconds>=get_file_or_folder_age(file_path):
                    remove_file(file_path)
                    deletedFiles+=1
else:
    print('path is not found')



