class University:
    def __init__(self,instname):
        self.instname="VTU"
        print("Welcome to ",self.instname)
    def test(self):
        print("Its a test function inside parent ")

class College(University):
    def __init__(self,name,collname,collId):
        self.name=name
        self.collname=collname
        self.collId=collId
    def __str__(self):
        return f"{self.collname}({self.collId}) is an institution under {self.name}"

c2=College(*,"New Horizon","1NH12LVS")
print(c2)
c2.test()

