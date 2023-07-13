#1.All words less than 5 letters
list1=["abc","banana","luminar","car"]
w3=[x for x in list1 if len(x)<5 ]
print("1.Words with less than 5 letters in ",list1," are :",w3)
#2.Numbers from 1-50 having 6 in them
n6=[num for num in range(1,51) if '6' in str(num)]
print("2.Numbers from 1-50 having 6 in them are : ",n6)
#3Change the case of words of alphabets in list
l=["abc","apple","chitra"]
uc=[str.upper(u) for u in l]
print("3.Case converted list is : ",uc)
#4add 2 list
l1=[4,5,6,9]
l2=[6,4,6,1]
sum=[l1[i]+l2[i] for i in range(0,len(l2))]
print("4.sum of",l1," and ",l2 ,"is" ,sum)
#5 find square of every num in list
l=[2,6,3,1]
sq=[x*x for x in l]
print("5.Square of ",l," is ",sq)
#6Find all num from 1-1000 that are divisible by 9
d_9=[n for n in range(1,1001) if n%9==0]
print("6 .Numbers that are from 1-1000 that are divisible by 9 are : ",d_9)
#7.Count the number of spaces in a string
str1="Hello! Have a wonderful day"
count=0
space=[count+1 for s in str1 if s==" "]
print("7 .the number of spaces in ",str1," is :",len(space))
#8List of consonents in given string
str2="yellow yaks like yelling"
con=[c for c in str2 if c not in ['a','e','i','o','u']]
print(" 8. List of consonents in",str2," is :",con)
#9get index and value as a  tuple for given list
l=["hi",4,80.99,"apple",('t','b''n')]
t=[ i for i in l ]
print("9.",(tuple(enumerate(t))))
# 10 Print numbers divisible by 2 and 5
n_2_5=[n for n in range(0,100) if n%2==0 and n%5==0]
print("numbers divisible by 2 and 5 are : ",n_2_5)





