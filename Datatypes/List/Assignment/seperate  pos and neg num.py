#WAP to seperate  pos and neg num from given list
list1=[]
plist=[]
nlist=[]
n=int(input("Enter the num of elements in list:"))
for i in range(n):
    k=int(input("Enter the num:"))
    list1.append(k)
print(list1)
print(type(list1))
for i in list1:
    #print(i)
    if (i)<0:
        nlist.append(i)
    else:
        plist.append(i)
print("p:",plist)
print("n:",nlist)


