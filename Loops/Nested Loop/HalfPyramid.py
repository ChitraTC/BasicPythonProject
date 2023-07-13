rows=int(input("Enter the number of rows:"))
for i in range (rows):
    for star in range(i+1):
        print("* ",end="")
    print()


#inverted
#rows=int(input("Enter the number of rows:"))
for i in range (rows,0,-1):
        for star in range(i):
            print("* ",end="")
        print()