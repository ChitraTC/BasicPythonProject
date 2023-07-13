# rows=int(input("Enter the number of rows:"))
# for i in range(0,rows):
#     for s in range(0,rows-i-1):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print(" *",end="")
#     print()

#reverse pyramid
# rows = int(input("Enter the number of rows:"))
# for i in range(0, rows):
#     for s in range(0,i+1):
#         print(" ",end="")
#     for j in range(0,rows-i):
#         print("*",end="")
#     print()

#reverse pyramid

rows=int(input("Enter the number of rows:"))
for i in range (rows):
    for space in range(rows-i):
        print(" ",end="")
    for star in range(i+1):
        print("* ",end="")
    print()


