#3.To check if triangle is equilateral ,isosceles or scalene
side1=int(input("Enter the length of side1:"))
side2=int(input("Enter the length of side2:"))
side3=int(input("Enter the length of side3:"))
if side1==side2==side3:print("Equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:print("Isosceles Triangle")
else:print("Scalene Triangle")