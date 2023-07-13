#5. List of even num between 4 to 30
def list_even_num(a,b):
    l=[]
    for i in range(a,b-1):
        if i%2==0:
            l.append(i)
        else:pass
    return l

start=int(input("Enter the starting range of list : "))
stop=int(input("Enter the ending range of list : "))
print("List of even numbers is : ",list_even_num(start,stop))

