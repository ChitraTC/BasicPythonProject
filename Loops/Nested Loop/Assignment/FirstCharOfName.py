#To print the character of first letter of your name :C
f=int(input("Enter the font size:"))
for i in range(f):
    for j in range(0,f-1):
        if i==0:
            print("* ",end="")
        if i==0 and j==f-2:
            print()
        elif j==0 and i!=0:
            print("*")
        elif i==f-2:
            print("* ", end="")



