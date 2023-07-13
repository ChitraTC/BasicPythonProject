#5 create dictionary by extracting key from given dictionary
# colour={
#     1:"red",
#     2:"blue",
#     3:"Orange",
#
# }
# print(dict.keys(colour))
# keys=[1,2,3]
# dict1={i:colour[i]for i in keys}
# print(dict1)
# # for i in keys:
# #     dict1={i:colour[i]}
# # print("dict1=",+str(dict1))
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
keys=dict.keys(sampleDict)
# print(keys)
# dict2={i:sampleDict[i]for i in keys}
# print(dict2)

for i in keys:
    dict1={i:sampleDict[i]}
print("dict1=",(dict1))
