#9.Get key of min val from dic
dict1={'a':5,'b':20,'c':0.5}
print(min(dict1,key=dict1.get))
dict2={1:'a',2:'A',3:"z"}
print(min(dict2,key=dict2.get))
dict3={"name":123,"age":25,"course":"xyz"}
x=dict3.values()
y=[]
for i in x:
    x=str(i)
    y.append(x)
print(min(y))