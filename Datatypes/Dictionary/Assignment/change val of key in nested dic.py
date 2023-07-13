#10. change val of key in nested dic

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
sampleDict["class"]["student"]["marks"]["history"]=20
print(sampleDict)

sc={'d1':{'name':"xy","age":12},
    'd2':{'pal':"56","qual":"btech"}
}
sc['d1']["age"]=55
print(sc['d1'])
