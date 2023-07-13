#Factorial using recurssion
def fact(n):
    if n==1:                      #return 1
        return 1
    else:
        print("n=",n)#3    2
        x=n*fact(n-1)#3*2!  2*1!
        print("x=",n)            #2*1 , 3*2*1 ,4*3*2*1 ,5*4*3*2*1=120
        return x
print(fact(6))