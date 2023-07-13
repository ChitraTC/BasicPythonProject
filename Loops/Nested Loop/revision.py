# #pyramid
# r=int(input("Enter the number of rows:"))
# k=1
# for i in range(r):
#     for s in range(0,r-i):
#         print(" ",end="")
#     #odd star(1,3,5,7,9)
#     for j in range(0,2*i+1):
#         print("*",end="")
#     #1,2,3,4,5 star
#     # for j in range(i+1):
#     #     print("* ", end="")
#     k=k+1
#     print()

#inverted
#r=int(input("Enter the rows:"))

# for i in range(r,0,-1):
#     for s in range(r-i):
#         print(" ",end="")
#     #natural 5,4,3,2,1
#     for j in range(i,0,-1):
#     #for odd stars 7,5,3,1
#     #for j in range(2*i-1):
#         print("* ",end="")
#     print()
#heart
# r=3
# for i in range(r):
#     for s in range(r-i):
#         print(" ",end="")
#     for j in range(2*i+5):
#         print("*",end="")
#
#     for s in range(5-(2*i),):
#         print(" ",end="")
#     for j in range(2*i+5):
#         print("*",end="")
#     print()
# r=10
# for i in range(r,0,-1):
#     for s in range(r-i+1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# #Hollow diamond
# r=int(input("Enter the val:"))
# for i in range(r):
#     for s in range(r-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         if (j==0) or (j==2*i):
#             print("*",end="")
#         else:print(" ",end="")
#     print()
# k=r-1
# for i in range(k,0,-1):
#     for s in range(r-i):
#         print(" ", end="")
#     for j in range(2*i-1):
#         if j==0 or (j==(2*i)-2):
#             print("*",end="")
#         else:print(" ",end="")
#     print()

#cross pattern
r=int(input("Enter the value:"))
for i in range(r):
    for s in range(i):
        print(" ",end="")
    for j in range(r-i):
        if (j == 0)or (j==r-i-1) :
            print(i," ",end="")
        else:
            print("  ",end="")
    print()

for i in range(r-1):
    for s in range(r-i-2):
        print(" ",end="")
    for j in range(i+2):
       if (j == 0) or (j ==i+1):
           print(r-i-2," ",end="")
       else:
             print("  ", end="")
    print()

