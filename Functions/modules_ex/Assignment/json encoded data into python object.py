#5. Convert json encoded data into python obj
import json
j_d='[1,2,3,4]'
print(type(j_d))
print(j_d)
p_o=json.loads(j_d)
print("Python objects :",p_o)
print(type(p_o))
