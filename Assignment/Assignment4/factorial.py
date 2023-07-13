# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)
# print("factorial of",n,"is:",fact)
n=int(input("Enter a number:"))
fact=1
for i in range(n,1,-1):
    fact=fact*(i)
    print(fact)
print("factorial of",n,"is:",fact)

#g=1
# for i in range(1,n+1):
#     if  i==n:
#         print(i,"=",end=" ")
#     else:
#         print(i,"x",end=" ")
# #     g=g*i
# # print(g)

# for i in range(1,n+1):
#     if i==5:
#         print(i,"=",fact)
#     else:
#         print(i,"x",end="")

for i in range(n,0,-1):
    if i == 1:
     print(i,"=",fact)
    else:
     print(i,"x",end="")






