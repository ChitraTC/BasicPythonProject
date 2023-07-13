rows=int(input("Enter the rows:"))
a=65
for i in range(rows):
    for space in range(rows-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(chr(a),end=" ")
        a+=1
    print()