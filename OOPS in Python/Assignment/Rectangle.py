"""
A class called Rectangle, which models a rectangle with a length and a width (in float), is designed as shown in the following class diagram. Write the Rectangle class.
 Attribute : length , width
Methods :
Rectangle()
Rectangle(length:float, width:float)
getLength()
getWidth()
getArea()
getPerimeter()

"""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_length(self):
        print(f"The lenght of rectangle is : {self.length}")
    def get_width(self):
        print(f"The width of rectangle is : {self.width}")
    def get_Area(self):
        area=self.length*self.width
        print(f"The area of rectangle is : {area}")
    def get_perimeter(self):
        perimeter=2*(self.length+self.width)
        print(f"The perimeter of rectangle is {perimeter}")

rec=Rectangle(2,4)
rec.get_length()
rec.get_width()
rec.get_Area()
rec.get_perimeter()

