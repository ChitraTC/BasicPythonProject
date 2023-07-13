import os
with open("test2.txt","r+") as fp:
    f3=open("test3.txt","w")

    for i in fp:
        f3.write(i)

