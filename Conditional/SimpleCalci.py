a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice=input("Enter your choice(+,-,*,/,**) :")

if choice=='+':
    print("The sum is",a+b)

elif choice=='-':
    print("The difference is",a-b)

elif choice=='*':
    print("The product is",a*b)

elif choice=='**':
    print(a ,"exponent", b ,"is:" , a**b)

elif choice=='/':
    print("The quotient is",a/b)

else:
    print("Invalid choice")

if a>b:print("a is larger")
else:print("b is larger")
