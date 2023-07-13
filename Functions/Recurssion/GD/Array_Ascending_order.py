#To check whether the array is in ascending order
def check(ls,l,n):
    ls=l[:]
    l.sort()
    # print("l=",l)
    # print("ls=",ls)
    if n==0:
        return
    else:
        if l[n-1]==ls[n-1]:
            check(ls,l,n-1)
            #print("Yes")
            return True

i=0
ls=[]
l=[22,20,19,15,5,2]
ls=l
n=len(l)
if(check(ls,l,n)):
    print("Yes the list is in ascending order")
else:print("No")
