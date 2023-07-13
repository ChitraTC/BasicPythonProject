str1=["john","","Jack","Ema","","Jins","Lina"]
str2=[]
# for i in str1:
#     print(i)
#     if i=="":
#         pass
#     else:
#         str2.append(i)
#
# print(str2)

#method2:
# str1.remove("")
# str1.remove("")
# print(str1)
#method 3:
for i in str1:
    if i.isspace():
        str1.remove(i)
print(str1)
