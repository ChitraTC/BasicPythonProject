#8.To find non repeating characters in a string
str1=input("Enter the string:")
str2=""
for i in str1:
    if str1.count(i)>1:
        pass
    else:str2+=i
print("The non-repeating characters in string are:",str2)