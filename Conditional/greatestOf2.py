# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if (a>b):
#     print("a is greater")
# else:
#     print("b is greater")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a>b and b>c):
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
elif (a==b==c):
    print("All are equal")
elif (a==b ):
    if (a>c):
     print("a is greater than c")
    else:print("c is largest")

elif (b==c):
    if (b>a):
     print("b is greater than c")
    else:print("c is largest")

elif (c==a):
    if (c>b):
     print("c is greater than a")
    else:print("a is largest")

# elif (a==b or b==c or a==c):
#     print("Two values are equal")
else:print("c is largest")