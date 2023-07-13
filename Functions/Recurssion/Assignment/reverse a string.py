#3.Reverse a string using recurssion

# def rev(s):
#     if len(s)==1:
#         return s
#     else:
#         x=rev(s[1:])+s[0]
#         print(x)
#         return x

# s=input("Enter a string : ")
# print("The reversed string is : ",rev(s))

def rev_r(s):                        #abc          bc       c
    size=len(s)                      #size=3       2        1            0
    if size==0:                                                          #size==0
        return                                                           #return to the caller program
    else:
        last_char=s[size-1]           #s[2]        s[1]     s[0]
        print(last_char,end="")       #c           b         a
        rev_r(s[0:size-1])            #s[0:2]      s[0:1}    s[0:0]
                                    #ab            a         size=0

st=input("Enter a string : ")
rev_r(st)