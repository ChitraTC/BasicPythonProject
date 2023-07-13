set1={1,2,3,5,"chitra"}
print(set1)
list1=[3,4,5]
set2=set(list1)
print(set2)

#to fetch the set
for i in set1:
   print(i)

#to fetch 5
if 5 in set1:
    print("yes")

#to add or remove elements to set
set1.add("Degish")
print(set1)
set1.remove(5)
print(set1)

set1.add("degi")
print(set1)
set1.add("degish")
print(set1)
#update
set3={"orange","apple","gauva"}
set1.update(set3)
print(set1)
#to update a list
l=[11,12,13.5,"peru"]
set4=set(l)
set1.update(l)
print(set1)
#remove,discard and pop
set1.remove(1)
set1.discard(2)
print(set1)
print(set1.pop())
print(set1.pop())
print(set1.pop())
#clear,del
# set1.clear()
# print(set1)
# del set2
# print(set2)
# del set1

#set operation
#1.Union
s1={1,2,3}
s2={2,"c","d","n"}
print(s1.union(s2))


#2.intersection
# print(s1.intersection(s2))
# print(s1)
# print(s1.intersection_update(s2))
# print(s1)

# #3 difference
# print(s2.difference(s1))
# print(s1)
# print(s1.difference_update(s2))
# print(s1)

# #4 symettric difference
# print(s1.symmetric_difference_update(s2))
# print(s1)

# isdisjoint()
print(s1.isdisjoint(s2))
#is subset
print(s1.issubset(s2))