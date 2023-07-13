# 1.find reminder of a=5 b=2
def rem(a):
    return lambda x:a%x
y=rem(5)
print("1.reminder of a=5 b=2 is ",y(2))

#2.Find double of a num
def double(x):
    return lambda a:x*a
d=double(5)
print("2.double of a 5 is ",d(2))

#3. add 3 num
def sum(x):
    return lambda a,b:a+b+x
s=sum(2)
print("3.Sum of 3 num = ",s(5,7))