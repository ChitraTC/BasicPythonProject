#LCM of two num using function
def LCM(a,b):
    if a>b:
        g=a
    else:
        g=b  #g=3
    while(1):
        if g%a==0 and g%b==0: #3%2!=0 3%3!=0 , 4%2==0 4%3!=0,5%2!=0 5%3!=0  , 6%2==0 6%3==0
            return g           #else part                                       return 6
        else:
            g=g+1              #g=3+1          g=4+1          g=5+1
    return g

#print(LCM(2,3))
#LCM using recurssion




# def lcm_r(a,b,g):                        #lcm_r(2,3,3)           lcm_r(2,3,4)           lcm_r(2,3,5)          lcm_r(2,3,6)
#     if g%a==0 and g%b==0:                #3%2!=0 and 3%3==0 F     4%2==0 and 4%3!=0 F   5%2!=0 ang 5%3!=0 F    6%2==0 and 6%3==0 T
#         return g                          #go to else                                                          return 6
#     else:return lcm_r(a,b,g+1)            #lcm_r(2,3,3+1)         lcm(2,3,4+1)          lcm(2,3,5+1)
#
#
# a=int(input("Enter the first num : "))
# b=int(input("Enter the sec num : "))
# if a > b:
#     g = a
# else:
#     g = b
# #print("LCM of ",a,"and ",b,"is :",lcm_r(a,b,g))




def lcm_r1(a,b,g):                        #lcm_r(3,5,5)           lcm_r(3,5,10)           lcm_r(3,5,15)
    if g%a==0 and g%b==0:                #5%3!=0 and 5%5==0 F     10%3!=0 and 10%5==0 F    15%3==0 and 15%5==0 T
        return g                          #go to else                                       return 15
    else:return lcm_r1(a,b,g+v)            #lcm_r(3,5,5+5)          lcm_r(3,5,10+5)


a=int(input("Enter the first num : "))#3  6  9 12 15
b=int(input("Enter the sec num : "))  #5 10 15 20 25
if a > b:
    g = a
else:
    g = b
v=g
print("LCM of ",a,"and ",b,"is :",lcm_r1(a,b,g))

