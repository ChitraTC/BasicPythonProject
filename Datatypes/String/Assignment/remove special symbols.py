#Remove special symbols / puntuation from a string
#str1 = "/*Jon is a developer & music director"
#ans: Jon is a developer music director
str1=input("Enter the string:")
str2=""
for i in str1:
    if i.isalpha() or i.isspace():
        str2=str2+i
print("The edited string is:",str2)


