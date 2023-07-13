class GrandFather:
    def ownHouse(self):
        print("Grad father's house")
class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")
class Son(Father):
    def ownBook(self):
        print("Its son's Book")

Raju=Son()
Raju.ownBook()
Raju.ownBike()
Raju.ownHouse()
