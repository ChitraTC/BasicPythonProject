#3.Function that accepts dufferent values as parameters and returns list
def gen_list(*a):
    l=list(a)
    return l

l1=[]
# for i in range(0,4):
#     a=input("Enter a value : ")
#     #l1.append(gen3
#     # _list(a))
# print(l1)


def food_items(*food):
    return list(food)
print(food_items('rice','dal',123,(1,2,3)))