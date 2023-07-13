#Reverse a num
n=int(input("Enter a num:"))
rev=0
while(n):
    rev=n%10
    print(rev,end="")
    n=n//10