#2.	To find if two strings are Anagrams or not.
#An anagram of a string is another string that contains the same characters,
# only the order of characters can be different. For example, “abcd” and “dabc”
# are an anagram of each other.
str1=input("Enter the string1:")
str2=input("Enter the string2:")
str3=""
c1=len(str1)
c2=len(str2)
c3=0
if c1==c2:
    for i in str1:
        for j in str2:
            if i==j:
                c3=c3+1
if c1==c3:
    print("Entered two strings are Anagrams")
else:
    print("Entered two strings are not Anagrams")


