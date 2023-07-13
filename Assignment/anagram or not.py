#3.To check whether entered string is anagram or not
str1=input("Enter the string 1:")
str2=input("Enter the string 2:")
l=len(str1)

if len(str1)==len(str2):
    for i in str1:
        if i in str2:
            l=l-1
    if l==0:print("Entered strings are Anagram")
    else:
        print("Entered strings are not Anagram")
else:
    print("Entered strings are not Anagram")


