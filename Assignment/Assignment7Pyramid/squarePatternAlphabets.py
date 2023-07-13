#Square Pattern Of Alphabets
rows=int(input("Enter the rows:"))
a=65
for i in range(rows):
    for j in range(rows):
        print(chr(a), " ", end="")
        a += 1
    print()

