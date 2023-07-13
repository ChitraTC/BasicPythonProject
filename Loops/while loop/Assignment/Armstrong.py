#Armstrong number or not
#A positive integer of n digits is said to be an armstrong numifthe sum of each digit of order n is equal to  the num
#ex:1,153,370,8208etc
n=int(input("Enter the number:"))
temp=n
l=len(str(n))
sum=0
while(n!=0):
    u=n%10
    sum=sum+(u**l)
    n=n//10  #1//10=0
print("sum=",sum)
if sum==temp:
    print(temp,"is an armstrong number")
else:print(temp,"is  not an armstrong number")
print(1%10)