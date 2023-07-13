#WAP to create list of even and odd num list from given list
list1=[1,2,3,4,5,6,7,8,9]
elist=[]
olist=[]
for i in list1:
    if i%2==0:
        elist.append(i)
    else:
        olist.append(i)
print("Even num  list is:",elist)
print("odd num list is:",olist)