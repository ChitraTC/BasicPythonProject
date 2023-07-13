string=input("Enter the String:")
#string="Python"
length=len(string)
print(string)
print(length)

for i in range(1,length+1):
    for j in range(0,i):
        print(string[j]," ",end="")
    print()
