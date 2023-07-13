#numbered cross pattern
f=int(input("Enter the font size:"))
i=0
j=f-1
m=f//2
n=k=1
#print(m)
for r in range(f):
    for c in range(f):
        if (r==i and c==j):
            if(c>m):
                print(n,end="")
                n=n+1
            else:
                print(n,end="")
                n=n-1
            i=i+1
            j=j-1
        elif (r==c):
                if (c < m):
                    print(k, end="")
                    k = k + 1
                else:

                    k = k - 1
                    print(k, end="")
        else:print(" ",end="")
    print()