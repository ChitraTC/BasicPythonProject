#10.Armstrong num
n=int(input("Enter the num:"))
t=n
l=len(str(n))
s=0
print("Base=",l)
while(n):
    dig=n%10
    s+=dig**l
    n=n//10
print("sum=",s)
if s==t:
    print(t,"is an Armstrong number")
else:
    print(t, "is not an Armstrong number")