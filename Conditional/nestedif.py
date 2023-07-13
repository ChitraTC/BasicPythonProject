# x=41
# if x<10:
#     print("Above 10")
#     if x<20:
#         print("and also above 20")
#     else:
#         print("below 20")
# else:
#     print("invalid")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b:
    if b>a:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")
