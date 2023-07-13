def fun(a,b):
    return a+b

def fun1(a):
    return len(a)

a=[1,2,3,4]
b=[8,6,7]
x=map(fun,a,b)

#Finding length of list
print(list(x))
a1=["Apple","Orange"]
x=map(fun1,a1)
print(list(x))

#using lambda
length=map(lambda x:len(x),a1)
print(list(length))

#converting to upper case
low=["abc","cde","efg"]
upper=map(str.upper,low)
print(list(upper))

#factorial of a number using reduce
from functools import reduce
#product=reduce((lambda x,y:x*y),4)
#print("Pr=",product)

n=5
print(reduce(lambda x,y:x*y,range(1,n+1)))

