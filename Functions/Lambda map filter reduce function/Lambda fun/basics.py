x=lambda a,b,c:(a+2)|(b*c)
print("x=",x(5,7,2))
y=lambda a :print(a)
y("chitra")

z=lambda:print("Python")
z()
#Sort using keys of tuple
t=[("eng",88),("science",90),("Kann",95),("Mal",99)]
t.sort(key=lambda a:a[0])
print(t)
#sort list of dict using lambda
d=[{1:"Apple",2:"carrot"},{1:"Orange",2:"beans"},{1:"Bananana",2:"Potato"}]
s_d=sorted(d,key=lambda a:a[2])
print(s_d)

#Extract date(y,m,d) time(h,m,s) using lambda
#t=2022-01-15 09:03:32

import datetime
now=datetime.datetime.now()
print(now)
year=lambda y:y.year
#another method
month=lambda :now.month
day=lambda y:y.day
t=lambda y:y.time()
print(now.year)
print(now.month)
print(now.day)
print(t(now))

print("month =",month())

#lambda inside fun
def myfun(n):
    print("Inside fun")
    return lambda a:a*n

x=myfun(2)#lambda a:a*2
print("In main")
print(x(5))#x=lambda 5:5*2
y=myfun(3)
print(y(5))
#
x=lambda a:a*2
print(x(2))

#create adder
def adder(x):
    def full_add(y,z):
        return x+y+z
    return full_add
s=adder(5)
print(s(2,3))
#Create adder using lambda
def l_add(x):
    return lambda y,z:x+y+z
sum=l_add(5)
print(sum(3,4))


