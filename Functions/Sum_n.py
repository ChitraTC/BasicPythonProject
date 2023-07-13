def sum_n(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
n=int(input("Enter the range:"))
print(sum_n(n))