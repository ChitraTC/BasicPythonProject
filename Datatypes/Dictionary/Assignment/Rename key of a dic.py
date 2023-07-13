#8.Rename key of a dic
# colour={
#     1:"red",
#     2:"blue",
#     3:"Orange",
#     4:"yellow",
#     5:"Green"
# }
# print("Original Dic:",colour)
# colour[10]=colour.pop(2)
# print("Renamed key Dic:",colour)

dict1={"name":123,"age":25,"course":"xyz"}
dict1['dep']=dict1.pop("name")
print(dict1)