#4.Convert python dict to json.Print the object with indent4
import json
p_o={'name':"Chitra",'age':12,'place':"Bangalore",'ph':12345}
j_d=json.dumps(p_o,sort_keys=True,indent=4)
print(j_d)
j=json.dumps(p_o)
print(j)

#sort key is used to sort keys according to ascii values