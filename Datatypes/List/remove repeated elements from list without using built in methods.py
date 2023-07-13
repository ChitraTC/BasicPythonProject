list1=["Let's","google","the","Pineapple","google","the"]
list2=[]
for i in list1:
    if i in list2:
        continue
    else:
        list2.append(i)
print(list2)