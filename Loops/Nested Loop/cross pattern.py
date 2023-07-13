# t=int(input("Enter the font size:"))
# i=0
# j=t-1
# for r in range(t):
#     for c in range(t):
#         if r==i and c==j:
#             print("*",end="")
#             i=i+1
#             j=j-1
#         elif(r==c):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

n=int(input("Enter the value of n:"))
for i in range(1,2*n):
    for j in range(1, 2 * n):
        if i==j or i+j==2*n:
            print(j, end="")
        else:
            print(" ",end="")
    print()


