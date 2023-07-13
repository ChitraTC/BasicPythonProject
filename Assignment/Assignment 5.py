#Number is prime or not
n=int(input("Enter the number"))
for i in range(2,n+1):
    if(n%i==0):
        print("Prime")
        break
    else:
        print("Not Prime")
        