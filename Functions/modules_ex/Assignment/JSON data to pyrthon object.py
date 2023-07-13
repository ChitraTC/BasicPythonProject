#1.convert json data to python object

import json
JSON_data='{"A":"Apple","B":"Ball","C":"Cat"}'
j_l='[1,2,3]'
print(type(JSON_data))
print("json data:",JSON_data)

python_obj=json.loads(JSON_data)
p=l=json.loads(j_l)

print("Python object :",python_obj)
print(type(j_l))