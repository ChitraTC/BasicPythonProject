# Number is prime or not
n = int(input("Enter the number::"))
if(n>1):
    for i in range(2, n ):
        if (n % i) == 0:
            print("Not Prime")
            break
    else:
        print(" Prime")



