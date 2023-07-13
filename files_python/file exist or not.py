#1.file exist
import os
def print1(a):
    if a==True:
        print("File exist")
    else:
        print("File doesn't exist")




path1=r"C:\Users\chitra\PycharmProjects\LearnPython\files_python\Nachu.txt"
x=(os.path.isfile(path1))
print1(x)

path2=r"C:\Users\chitra\PycharmProjects\LearnPython\files_python\Saachu.txt"
y=(os.path.exists(path2))
print1(y)

#2.Toget file size
path1=r"C:\Users\chitra\PycharmProjects\LearnPython\files_python\Nachu.txt"
print(os.path.getsize(path1))

# To delete lines from a file
# path1=r"C:\Users\chitra\PycharmProjects\LearnPython\files_python\Nachu.txt"
# x=(os.path.isfile(path1))

f1=open("Nachu.txt","r+")
line=f1.readlines()
f1.seek(4)
print(f1.read())
