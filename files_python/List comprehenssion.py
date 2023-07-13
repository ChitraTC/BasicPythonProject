# #Seperate even and odd num from list
l1=[1,2,3,4,5,6,7,8,9,10]
# le=[]
# lo=[]
# for i in l1:
#     if i%2==0:
#         le.append(i)
#     else:lo.append(i)
# print("le=",le)
# print("lo=",lo)

obj=[(i,'even' if i%2==0 else 'odd')for i in l1]
print(obj)
print()
print(list(enumerate(obj)))

#ex 2:names containg 'a'
fruits=['apple','egg','orange','grapes']
n=[]
for x in fruits:
    if 'a' in x:
        n.append(x)
print("new list = ",n)

newlist=[x for x in fruits if'a' in x]
print(newlist)

#ex3:print prime num:
l=[1,2,3,4,5,6,7,8,9,10]
prime_num=[n for n in l if all(n%i!=0 for i in range(2,n)) and n>1]
#prime=[n for i in l if (n%i!=0 for i in range(2,n))]
print(prime_num)
#prime=((n,))
print()
nl=[]
for n in l:
    if n%3==0:
        nl.append(n)
print("new list = ",nl)
div_3=[n for n in l if n%3==0]
print(div_3)