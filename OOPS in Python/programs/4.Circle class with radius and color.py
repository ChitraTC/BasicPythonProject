import math
from colorama import Fore
class Circle:
    import math
    from colorama import Fore
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color
        print(f"{Fore.YELLOW}It is a {self.color} Circle")
    def getRadius(self):
        print(f"The radius of circle is : {self.radius}")
    def getCircumference(self):
        Circumferance=2*3.14* self.radius
        print(f"The circumferance of circle is  {Circumferance}")
    def getArea(self):
        Area=3.14* self.radius * self.radius
        print(f"The area of circle is {Area}")

circle=Circle(4,"YELLOW")
circle.getRadius()
circle.getCircumference()
circle.getArea()