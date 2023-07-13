n=10
while(n<=100):
    i=2
    while(n>i):
        if(n%i==0):
            break
        else:i=i+1
    if(i==n):
        print(n, " ", end="")
    n=n+1






