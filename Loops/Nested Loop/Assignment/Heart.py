# k=10
# n=m=k//2
# sp=5
# spiv=19
# for i in range(3):
#     for s in range(4-i-1):
#         print(" ",end="")
#     for star in range(0,n):
#         print("*",end="")
#     n=n+2
#
#
#     for s in range(0,sp):
#         print(" ",end="")
#     sp=sp-2
#     for star in range(0,m):
#         print("*",end="")
#     m=m+2
#     print()
#
# for i in range(10,0,-1):
#     for s in range(10-i+1):
#         print(" ", end="")
#
#     for star in range(spiv,0,-1):
#         print("*", end="")
#     spiv=spiv-2
#     print()





#heart
r=3
for i in range(r):
    for s in range(r-i):
        print(" ",end="")
    for j in range(2*i+5):
        print("*",end="")

    for s in range(5-(2*i),):
        print(" ",end="")
    for j in range(2*i+5):
        print("*",end="")
    print()
r=10
for i in range(r,0,-1):
    for s in range(r-i+1):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()