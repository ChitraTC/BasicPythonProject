#Greatest Common Divisor
# import math
# n1=int(input("Enter num1:"))
# n2=int(input("Enter num2:"))
# print("GCD:",math.gcd(n1,n2))
# print("LCM:",math.lcm(n1,n2))

#method 2
n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
if n1>n2:
    max=n1
    min=n2
else:
    max=n2
    min=n1
def gcd(max,min):
    if min==0:
        return max
    else:
        return gcd(min,max%min)
gcd=gcd(max,min)
print("gcd=",gcd)

