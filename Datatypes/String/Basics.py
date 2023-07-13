# s="Hello# w   #  orld55"
# print(type(s))
# # print(s[::-1])
# # print(s[-1:-10:1])
# # print(s[4:1:-1])
# # print(s[::-1])
# # print(s[0])
# # s[0]='M'
# # print(s[::1])
# # print(s[-1:-5:-2])
# print(s.capitalize())
# print(s.center(20))
# print(s.count('H'))
# print(s.format(p=3))
# print(s.index('H'))
# print(s.find("w"))
# print(s.isalnum())
# print(s.isalpha())
#
#
#
#
#a="banana"
# i=0
# while(len(a)>i):
#     #print('{}{}'.format(i,a[i]))
#
#     #print(i,a[i])
#     print(f"{i}{a[i]}")
# print(a.replace("n","b"))
# bags=3
# apples_in_bag=12
# print(f"there are total of {bags*apples_in_bag} apples")
# format('bags*apples_in_bag','90')
# x=print(s.title())
# print(x)
# l=["AM","Ag","ah"]
# print("*".join(l))
# print(s.split("#    ",1))
# s="Jamesl"
# l=(int(len(s)))
# print(l)
# print(s[0]+s[int(l/2)]+s[-1])
# #2
# s1="hello"
# s2="World"
# l1=(len(s1))
# m=int(l1/2)
# print(m)
# print(s1[:m]+s2+s1[m:])

#3
# s="HeLLO World"
# n=m=o=""
# for i in s:
#     if i.islower():
#         n+=i
#         print(n)
#     else:
#         m+=i
#     # else:
#     #     o+=i
# print(n+m)

#4
s="p@#$yn26at^i5ve"
l=d=sym=0
for i in s:
    if i.isalpha():
        l=l+1
    elif i.isdigit():
        d+=1
    else:
        sym+=1
print("number of letters =",l)
print("number of digits =",d)
print("number of sym =",sym)