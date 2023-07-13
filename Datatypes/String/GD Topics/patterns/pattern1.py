r=int(input("Enter the row:"))
# c=0
# for i in range(r):
#     for j in range(i+1):
#         print(i*j,end=" ")
#
#     print()

for i in range(1,r+1):
   for j in range(1,r+1):
       if i==r or j==r:
           print(r,end=" ")
       elif i==j:
           print(j,end=" ")
       else:print(j,end=" ")
   print()



