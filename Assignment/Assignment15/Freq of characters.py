#5. frequency of characters
str1=input("Enter the string:")
l=int(len(str1))
c=0
str2=""
while(l):
    for i in str1:
        if i in str2:
            pass
        else:
            c=str1.count(i)
            str2+=i
            print(i,"is repeated",c,"times")
    l=l-1


