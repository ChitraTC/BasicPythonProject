#4. Initialize dict with default value
# dict1={1:"red",2:"Blue",3:"green"}
# x=dict1.setdefault(3,"Grey")
# print(x)
# print(dict1)
# y=dict1.setdefault(4,"black")
# print(y)
# print(dict1)

#method2

keys=["dict1","dict2"]
default={"place":"Bangalore",'pf':897}
res=dict.fromkeys(keys,default)
print(res)