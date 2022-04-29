import os
path=r'D:\cursopy'
b=os.listdir(path)
path_len_org=len(b)
def file_check():
    while 1:
        b=os.listdir(path)
        path_len_final=len(b)
        if path_len_org<path_len_final:
            print("Added")
            return "A file is added"    
        elif path_len_org>path_len_final:
            print("Delete")
            return "A file is removed"
        else:
            pass
file_check()