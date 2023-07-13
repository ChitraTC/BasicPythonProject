#program to display all prime numbers within a range
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for n in range(lower,upper+1):
    if(n>1):
        for i in range(2,n):
            if (n%i==0):
                break
        else:print(n)
