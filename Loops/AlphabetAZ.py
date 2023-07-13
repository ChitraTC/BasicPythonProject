#A=65 to Z=90
# for i in range(65,97+26):
#     print(chr(i),"",end="")
# print()
# #a=97
# for i in range(97,97+26):
#     print(chr(i),"",end="")

# import string
# for i in string.ascci_uppercase:
#     print(i,end=" ")

rows=int(input("Enter the rows:"))
a=65
for i in range(rows):
    for j in range(i+1):
            print(chr(a)," ",end="")
            a+=1
    print()


