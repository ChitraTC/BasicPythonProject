#9.Circular rotation of an array by k positions
str1=input("Enter the array:")
l=int(len(str1))
print(l)
l1=list(str1)
print("l1:",l1)
l2=l1
k=int(input("Enter value of k:"))
m=k
for i in range(k):
    temp=l2[len(l1)-1]
    for j in range(len(l1)-1,0,-1):
        l2[j]=l2[j-1]
    l2[0]=temp

print("Circular rotation of ",str1," by", m ,"positions is:",l2)

