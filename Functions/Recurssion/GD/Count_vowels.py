#Count number of vowels using 2 fun isvowel and countvowel
# a = e = i = o = u = 0
# def isvowel(s):
#     a = e = i = o = u = 0
#     if len(s)==0:
#         return
#     x=s[0]
#     if x in ['a',"e",'i','o''u']:
#         a,e,i,o,u=countvowel(s[0])
#         if a==1:a=a+1
#         if e== 1:e=e+1
#         if i==1:i=i+1
#         if o==1:o=o+1
#         if u==1:u=u+1
#     isvowel(s[1:])
#     return (a,e,i,o,u)
# def countvowel(s):
#     a = e = i = o = u = 0
#     if s=='a':
#         a=a+1
#     if s=='e':
#         e=e+1
#     if s=='i':
#         i=i+1
#     if s=='o':
#         o=o+1
#     else:u=u+1
#     return a,e,i,o,u
#
# a=e=i=o=u=0
# s=input("Enter the string :")
# (a,e,i,o,u)=isvowel(s)
# print("a=",a)
# print("e=" ,e)
# print("i=",i)
# print("o=",o)
# print("u=",u)
count=0
def isvowel(s):
    global count
    c=0
    if len(s)==0:
        return
    else:
        if s[0] in ['a','e','i','o','u']:
            c=countvowels(c)
            if (c):
                count=count+1
        isvowel(s[1:])
        return count
def countvowels(c):
    c=c+1
    return c

s=input("Enter the string : ")
c=isvowel(s)
print("There are ",c," vowels in string ",s)

