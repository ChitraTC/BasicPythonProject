#Accept 10 numbers from the user and display their average
sum=0
for i in range(0,10):
    n=int(input("Enter 10 numbers:"))
    sum=sum+n
average=sum/10
print("Average of 10 numbers is:",average)