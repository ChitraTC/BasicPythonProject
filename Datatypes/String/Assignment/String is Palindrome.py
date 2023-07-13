#4.	To check if a string is palindrome or not
str1=input("Enter the string1:")
str2=str1[::-1]
print("The reverse of",str1,"is",str2)
if str1==str2:
    print("The entered string is palindrome ")
else:print("The entered string is not palindrome ")
