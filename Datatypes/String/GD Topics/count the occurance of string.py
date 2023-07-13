#1
# str1="Welcome to USA.USA is awesome"
# s="USA"
# c=str1.count("USA")
# print("USA occurs",c,"times")

#2 input=restart output:resta$t
# str1="restart"
# c=str1[0]
# str2=""
# for i in str1[1:]:
#     if i.find(str1):
#         i=i.replace(c,"$",2)
#         str2+=i
# print(c+str2)

#3input s1="hello",s2="world",Output:wollo herld
# s1="hello"
# s2="world"
# s3= s1+" "+s2
# print(s3)
# s3= s2[0:2]+s1[2::]+" "+s1[0:2]+s2[2::]
# print(s3)

# #4 add ing to string if l>2
# str1=input("Enter the string:")
# str2=""
# l=len(str1)
# if int(l)>2:
#     str2=str1+"ing"
# else:
#     str2=str1
# print(str2)

#5 count vowels in the entered string;

list1=['a',"e","i","o",'u']
str1=input("Enter the string:")
count=0
print("The vowels are:",end=" ")
for i in str1:
    if i=='a':
        count+=1
        print("a",end=" ")
    if i=='e':
        count+=1
        print("e", end=" ")
    if i=='i':
        count+=1
        print("i", end=" ")
    if i=='o':
        count+=1
        print("o", end=" ")
    if i=='u':
        count+=1
        print("u", end=" ")
print()
print("vowel count is:",count)






