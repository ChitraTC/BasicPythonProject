#5.string_palindrome

def rev(s):
    if len(s)==1:
        return s
    else:return rev(s[1:])+s[0]

s=input("Enter the string :")
s1=rev(s)
print(s1)
if s==s1:
    print("palindrome")
else:print("Not Palindrome")