#2.Reverse a number
def rev(num):
    l=len(str(num))
    if num==0:
        return
    else:
        d=num%10
        print(d,end="")
        num=num//10
        l=l-1
    return rev(num)


num=int(input("Enter a num : "))
rev(num)