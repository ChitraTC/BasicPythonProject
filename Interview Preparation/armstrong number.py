#153
n=int(input("Enter the number:"))
c=len(str(n))
t=n
sum=0
print(c)
while(n):
    d=n%10
    print("d=",d)
    sum=sum+(d**c)
    print("sum=",sum)
    # print(sum)
    n=n//10
    print("n=",n)
print("sum =",sum)
if sum==t:
    print(t,"is armstrong")
else:
    print(t, "is not armstrong")



