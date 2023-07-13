def max_3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a or b>c:
        return b
    else:return c
print(max_3(9,5,16))

def max_fun(a,b,c):
    return(max(a,b,c))
print(max_fun(11,25,2))

def max_list(n):
    j=0
    for i in n:
        if i>j:
            j=i
        else:pass
    return i
n=[11,25,50]
print(max_list(n))

def max_list_fun(n):
    print(max(n))
n = [11, 25, 50,95]
max_list_fun(n)

