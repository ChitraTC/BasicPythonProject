#4 median of three values
a=int(input("Enter the first num:"))
b=int(input("Enter the sec num:"))
c=int(input("Enter the third num:"))

if a<b and b<c:
    print(b,"is the median")
elif a>b and a<c:
    print(a,"is the median")
else:print(c,"is the median")