#3.To calculate the length of a string without using a library function.
str1=input("Enter the string1:")
c=0
print("Length of string using lib func is:",len(str1))
for i in str1:
    c=c+1
print("The length of a string without using a library function is:",c)