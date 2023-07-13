#1.to multiply all numbers in the list

def mul_list(n):
    p=1
    for i in n:
        p=p*i
    return p

n=[1,2,3,4,5]
print("product of all numbers in list is :",mul_list(n))
