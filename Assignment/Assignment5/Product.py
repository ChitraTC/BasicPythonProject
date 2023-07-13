#program to display product of the digits of a number accepted from the user.
# d=int(input("Enter the number of digits"))
# n=int(input("Enter the number:"))
# product=1
# for i in range(1,d+1):
#     if(n>0):
#         rem=n%10
#         product=product*rem
#         n=n//10
# print(product)
n=(input("Enter the number:"))
p=1
for i in range(len(n)):
    print(i)
    p=p*int(n[i])
print(p)
