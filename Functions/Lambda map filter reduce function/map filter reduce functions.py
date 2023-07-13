"""
lambda x:a+x -It takes any number of arguments but returns only one variable
map(func,iterables)here each element of tuple is mapped with function add which returns the double of each element
filter(func,iterables)geneterates a list of values that return true when the func is called
reduce(func,iterables)-it apllies a provided function to iterables and return a single value as output
"""

#map(func,iterable)
def add(n):
    return n+n
num=(1,3,4,5)
res=map(add,num)# here each element of tuple is mapped with function add which returns the double of each element
print(list(res))

#lambda within map function
num1=[1,2,3]
num2=[4,5,6]
res=map(lambda x,y:x+y,num1,num2)
print(list(res))

#filter
def func(x):
    if x>=3:
        return x

y=filter(func,(1,2,3,4,5))
print(y)
print(list(y))

#to filter vowels from a string
def func(str1):
    vowels=['a','e','i','o','u']
    if str1 in vowels:
        return True
    else:
        return False
str1=['p','y','t','h','o','n','e']
filtered=filter(func,str1)
print(list(filtered))
str2="Chitra"
filtered=filter(func,str2)
print(list(filtered))

#reduce
product=1
list=[1,2,3,4]
for num in list:
    product=product*num
print("P=",product)
#using reduce
from functools import reduce
product=reduce((lambda x,y:x*y),[1,2,3,4])
print("Pr=",product)


