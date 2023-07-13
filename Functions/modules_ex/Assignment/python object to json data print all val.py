#3.python object to json data print all values
import json
python_obj={'A':"Apple","B":"Ball",'c':"Cat"}
print(type(python_obj))
print("Python object :",python_obj)
JSON_data=json.dumps(python_obj)
print("json data:",JSON_data)
print(type(JSON_data))
print(JSON_data[0::])

