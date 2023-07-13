a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a>b and b>c) or ((a==b)and a>c):
    print(a," is largest")
elif (b>a and b>c) or((b==c)and b>a):
    print(b," is largest")
elif (c>a and c>b) or((a==c)and c>b):
    print(c," is largest")
elif (a==b==c):
    print("All are equal")
else :print("Error")