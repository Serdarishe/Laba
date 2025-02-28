import os


#1
def list_content(path):
    all_items = os.listdir(path)

    print(os.path.exists(path))

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("all items: ", all_items)
    print("directories: ", directories)
    print("files: ", files)

path = "."
list_content(path)

#2
path = "."

print("Exist:", os.access(path, os.F_OK))
print("Readable:", os.access(path,os.R_OK))
print("Writeable:", os.access(path,os.W_OK))
print("Executable:", os.access(path,os.X_OK))

#3
path = '/Users/Serdar/Desktop/VSCODE'
if(os.access(path, os.F_OK)):
    filename = os.path.basename(path)
    print(filename)
else:
    print('Exist:', os.access(path, os.F_OK))

