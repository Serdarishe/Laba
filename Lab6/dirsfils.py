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

#4
with open('lab6/papapa.txt','r') as papapa:
    cnt = 0
    for i in papapa:
        cnt +=1

print(cnt)


#5
lst = [0,1,2,3,4,5,6,7,8,9]

file = 'lab6/task5.txt'
with open(file,'w') as f:
    for i in lst:
        f.write(str(i)  + "\n" +((i+1) *" "))

#6
for i in range(65,91):
    f = chr(i)
    file = f"lab6/{f}.txt"
    try:
        with open(file, 'x') as f:
            print(f"file {file} created!")
    except FileExistsError:
        print(f"file {file} already exists!")

#7
file1 = 'lab6/papapa.txt'
file2 = 'lab6/A.txt'

with open(file1, 'r') as f1:
    data = f1.read()

with open(file2, 'w') as f2:
    f2.write(data)

#8
def deldel(file):
    if not os.path.exists(file):
        print (f"{file} doesn't exist")
        return
    if not os.access(file , os.W_OK):
        print(f"can't access {file}")
        return
    try:
        os.remove(file)
        print(f"{file} deleted")
    except Exception:
        print(f"can't delete {file}")

file = 'lab6/file.txt'
deldel(file)