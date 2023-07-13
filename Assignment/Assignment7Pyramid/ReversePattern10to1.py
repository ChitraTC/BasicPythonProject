#Reverse Pattern 10-1
rows=int(input("Enter the number of rows:"))
for i in range(rows,0,-1):
    for n in range(i,0,-1):
        print(n,end=" ")
    print()