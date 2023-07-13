# Python program to get the Fibonacci series between 0 to 50.
n1=0
n2=1
nth=int(input("Enter the range:"))
if (nth==0):
    print("Enter a valid range")
elif (nth==1):
    print(n1,n2,end="")
else:
    print("Fibonacci series between 0 to ",nth ,"is:")
    print(n1,n2)
    # print(n2)
    n = 0
    for i in range(0,50):
         n = n1 + n2
         n1=n2
         n2=n
         if (n>=nth):
             break
         print(n,end=" ")





