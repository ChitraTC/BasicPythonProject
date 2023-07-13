#1. Addition two num
def sum(x):
        return lambda a:a+x
s=sum(3) #lambda a:a+3
print("1.sum(3+2)",s(2))


#2. Product of 3 nos
def pro(x):
    return lambda a,b:x*a*b
p=pro(2)
print("2.Product=",p(3,4))



#3find num is even or odd
x= lambda a:a%2==0
#print(x(4))
if x(4)==True:
    print("3.even")
else:print("3.odd")

#4. Check a substring is present
s1="today is a beautiful day"
s2="is"
st=lambda st:s2 in s1
if st==True:
    print("4.Present")
else:print("4.Not Present")

#5 Find num greater than 15 in list
l=[1,16,17,5,90]
x=list(filter(lambda a:a>15,l)) # Return an iterator yielding those items of iterable for which function(item)is true.
print("5.Numbers greater tha 15 are :",x)

#6Numbers divisible by 4 in list
l1=[4,15,20,6,24,28,72]
x=list(filter(lambda a:a%4==0,l1))
print("6.Numbers divisible by 4 in list are :",x)
