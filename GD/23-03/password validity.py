#1.Password validity
"""
at least 1 letter[a-z] ,[A-Z],1num[0-9],1 special character[$#@]
min len 6
max 16
"""
password=input("Enter the password:")
l=len(password)
print(l)
a=b=c=d=e=0
if l>=6 and l<=16:
    for i in password:
        if i.isdigit():
            a=a+1
            #print("digit:",a)
        elif i.isupper() :
            b=b+1
            #print("upper:", b)
        elif i.islower():
            c=c+1
            #print("lower:", c)
        elif i=='$' or i=='#' or i=='@':
            d=d+1
            #print("special:", d)
        else:e=e+1
    if a>=1 and b>=1 and c>=1 and d>=1 and e==0:
        print("The entered password is valid")
    else:
        print("Invalid password")
        if a==0:print("Enter atleast a digit in your password")
        if b== 0: print("Enter atleast a uppercase in your password")
        if c== 0: print("Enter atleast a lowercase in your password")
        if d== 0: print("Enter atleast one special character(@,#,$) in your password")
        if e>=1: print("No special character other than @,#,$ are allowed")
else:
    print("Enter a valid password")
