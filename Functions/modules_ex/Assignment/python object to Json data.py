#2.Convert python object to JSON data
import json
python_obj={'A':"Apple","B":"Ball",'c':"Cat"}
python_obj1=[1,'A',3,4]
print(type(python_obj))
print("Python object :",python_obj)
JSON_data=json.dumps(python_obj)
print("json data:",JSON_data)
print(type(JSON_data))
# print(type(python_obj1))
# print("Python object1 :",python_obj1)
# JSON_data1=json.dumps(python_obj1)
# print("json data1:",JSON_data1)
# print(type(JSON_data1))