n=int(input("Enter a number:"))
l=len(str(n))
print("length of number:",l)
while(l!=0):
    rev=int(n%10)#3,2,1
    print(rev,end="")#321
    n=n//10#12,1,
    #print(n)
    l=l-1#3-1=2,2-1=1,1-1=0