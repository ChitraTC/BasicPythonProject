import json
# print(dir(json))
#parsing python to json
x={1:"a",2:"b"}
print(type(x))
print("x=",x)
y=json.dumps(x)
print(type(y))
print("y=",y)

#parsing json to python
x='{"name":"chitra","age":12}' #json str data
# print(type(x))
# print("x=",x)
y=json.loads(x)
print(type(y))
print("y=",y)