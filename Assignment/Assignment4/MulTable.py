# Write a program to print multiplication table of a given number
n=int(input("Enter the multiplier:"))
c=int(input("Enter the count:"))
for i in range(c+1):
    p=n*i
    print(n,"*",i,"=",p)
