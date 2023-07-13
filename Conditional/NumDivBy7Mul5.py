num=int(input("Enter the number:"))
if num%7==0 and num%5==0:
    print(num,"is divisible by 7 and it's a multiple of 5")

elif (num%7==0 and not(num%5==0)):
    print(num,"is  divisible by 7 and it's  not a multiple of 5")

elif (num%7!=0 and (num%5==0)):
    print(num,"is not divisible by 7 and it's  a multiple of 5")


else:print(num,"is not divisible by 7 and it's not a multiple of 5")