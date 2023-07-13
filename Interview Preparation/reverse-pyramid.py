# reverse pyramid
# rows = int(input("Enter the number of rows:"))
# for i in range(0, rows):
#     for s in range(0,i):
#         print(" ",end="")
#     for j in range(0,rows-i):
#         print("*",end=" ")
#     print()
#9,7,5,3,1
rows = int(input("Enter the number of rows:"))
for i in range(rows, 0):
    for s in range(0,i):
        print(" ",end="")
    for j in range(0,(2*i)-1):
        print("*",end=" ")
    print()



