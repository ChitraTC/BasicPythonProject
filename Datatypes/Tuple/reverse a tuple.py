# tup=(1,2,3,"k","l",[1,2.3,3,"k"])
# print(tup[::-1])

#2.Access value 20 from tuple
# tup=("Apple",[10,20,30],(5,12,25))
# print(tup[1][1])
#
# #3.Swap 2 tuple contents
# tup1=(11,22)
# tup2=(10,40)
# tup3=()
# tup3=tup1
# tup1=tup2
# tup2=tup3
# print("tuple1",tup1)
# print("tuple2",tup2)
# #method 2
# tup1,tup2=tup2,tup1
# print("tuple1",tup1)
# print("tuple2",tup2)

#4 unpacking of tuple
# tuple1=("Apple",[10,12,14],(5,6,7))
# (x,*y)=tuple1
# print(*y)
# x,y,z=3,4,7
# print(z)

#5.wap to check whether an element exists within a tuple
# tup1=("Apple",[10,20,30],(5,12,25),1,5,6,7)
# ele=input("Enter the element to be checked:")
# if ele in tup1:
#     print("Present")
# else:print("no")

#convert tup to str
# tup=("s","t","r","i","n","g")
#
# x="".join(tup)
# print(x)
# #to print corresponding index
# tup=("s","t","r","i","n","g")
# # c=0
# # for i in tup:
# #     print("index of",i,"is",c)
# #     c=c+1
# y=enumerate(tup)
# print(list(y))
tup3=(1,2,3)
y=all(tup3)
print(y)
tup2=(1,0)
x=any(tup2)
print(x)
print(min(tup3))
tup4=("apple","banana","Orange")
print(min(tup4))


