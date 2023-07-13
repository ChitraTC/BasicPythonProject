import os
#1.number of words in text file
with open("test3.txt","r+") as fp:
   k=fp.read()
   print(k)
   c=u=a=0
   for ch in k:
       if ch==" ":c=c+1
       else :pass
   print("1. Number of words n text file is : ",c)

#2.Counting upper case characters
   for i in k:
       if i.isupper():
        u=u+1
   print("2.Upper case count= ",u)
fp.close()
#3.Counting number of lines starting with  A
with open("test3.txt","r+") as fp:
   print(fp.readlines())
   #print(l)
   for i in fp.readlines(4):
        if i=='\n':

            a=a+1
   print(a)



