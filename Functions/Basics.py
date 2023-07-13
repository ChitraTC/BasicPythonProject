#basic function
def test():
    print("Hello")
# test()
# #passing arguments
def sum():
     a=int(input("Enter a num:"))
     b=13
     c=a+b
     print(c)
     return(c)

def pro(a,b):
    # a=5
    # b=12
    print("c=",a*b)
    return(a*b)

# pro(5.5,6)
# s=sum()
# p=pro(2,3)
# d=s-p
# print("difference=",d)

def s1(a,b,c,d):
    e=a+b
    f=c+d
    g=a*b
    return(e,f)
# print(s1(1,2,3,4))
# x,y=s1(1,2,3,4)
# print("x=",x)
# print("y=",y)

#arbitrary argument
def fun1(*names):
    print("Hello",names,",how are u people doing")
# fun1("Degish","Chitra","and","Nakshatra")

#keyword argument
def child(child1,child2,child3):
    print("Youngest child="+child3)
child(child3="surya",child2="Anvika",child1="Nachu")

#Arbitrary Keyword Argument
def my_fun(**name):
    print("Last name="+name["lname"])
    print("First name=" + name["fname"])
my_fun(fname="Chitra",lname="Degish")

#default value
def my_fun1(country="India"):
    print("I am from "+country)
my_fun1()
my_fun1("UK")

# def employee(**emp):
#     print("Employee Name is" ,{}," With an id of",{} +emp[Name],+emp[ID])
#
# employee(Name="Chitra",ID=457,Salary=1234567)
def food_items(food):
    for i in food:
        print(i,end=" ")
food=["biriyani","rice","veg"]
# food_items(food)
# for i in food:
#     x = print(food_items(food))
from Sum_n import sum_n
print*++-99sum_n()




