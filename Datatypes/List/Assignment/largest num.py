#WAP to find largest num in a given list
list1=[1,2,9,4,5]
big=0
for i in list1:
    if i>big:
        big=i
    else:pass
print("big=",big)

print(max(list1))
l=(list1.sort())
print(l)
