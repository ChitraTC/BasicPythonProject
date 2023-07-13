#WAP to find common num from 2 list
list1=[1,2,3,9,12]
list2=[3,4,9,11,5]
listc=[]
for i in list1:
    for j in list2:
        if j ==i:
            listc.append(j)
        else:pass
print(listc)

