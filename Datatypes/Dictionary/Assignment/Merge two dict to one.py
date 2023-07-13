#2.Merge two python dictionaries into one
dict1={1:"red",2:"Blue",3:"green"}
dict2={4:"yellow",5:"orange",6:"Black"}
print(dict1.update(dict2))
print(dict1)
print(dict1|dict2)