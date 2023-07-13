# n=int(input("Enter the value of n:"))
# sum=0
# if(n>0):
#     sum=(n*(n+1))/2
#     print(sum)
# else:
#     print("no value")

# using for loop
print("Sum of n natural numbers")
n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)