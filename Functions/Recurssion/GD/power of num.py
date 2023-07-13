#1. power of num using recurssion

def power(base,exp):
    if exp==0:
        return 1
    else:
        res=base*power(base,exp-1)
        return res


base=int(input("Enter the base :"))
exp=int(input("Enter the exponent :"))
print(base," raise to ",exp," is : ",power(base,exp))