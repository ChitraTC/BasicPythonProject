#Product of two num using recurssion
def pro(a,b,n):     #2,3,3
    if a==0 or b==0:
        return 0
    elif n==1:
        return a
    else:
        s=a+pro(a,b,n-1)   # s=2+p(2,3,2)  ,
                                                # s=2+p(2,3,1)here n==1 returns a=2
        print("s=",s)                          #returns2+2=4
                            # returns2+4=6
        return s


a = int(input("Enter the first num : "))
b = int(input("Enter the sec num : "))
n=b
print("Product of",a,'and',b, "is : ",pro(a,b,n))