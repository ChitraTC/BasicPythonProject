#given pattern,HourGlass
rows=int(input("Enter the number:"))
for i in range(rows,0,-1):
    for space in range(rows-i):
        print(" ",end="")
    for star in range(i):
        print("* ",end="")
    print()
for i in range(0,rows):
    for space in range(rows-i-1):
        print(" ",end="")
    for star in range(i+1):
        print("* ",end="")
    print()
