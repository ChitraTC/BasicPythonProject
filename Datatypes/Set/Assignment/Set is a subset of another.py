#10 to check if a Set is a subset of another
set1={1,2}
l=len(set1)
print(l)
set2={1,2,3,4,5,}
c=0
for i in set1:
    if i in set2:
        print(i ,"in set2")
        c+=1
    else:print(i ,"not in set2")
if l==c:
    print(set1,"is subset of",set2)
else: print(set1,"is not subset of",set2)