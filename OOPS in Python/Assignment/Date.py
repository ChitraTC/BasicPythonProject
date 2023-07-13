"""
A class called Date, which models a calendar date, is designed as shown in the following class diagram. Write the Date class.



"""
class Date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    def get_day(self):
        print(f"Day : {self.day}")
    def get_month(self):
        print(f"Month : {self.month}")
    def get_year(self):
        print(f"Year : {self.year}")
    def set_day(self,d):
        self.day=d
    def set_month(self,m):
        self.month=m
    def set_year(self,y):
        self.year=y
    def set_date(self,d,m,y):
        self.day = d
        self.month = m
        self.year = y
    def tostring(self):
        print(f"Date : {self.day}/{self.month}/{self.year}")
d=Date(8,9,2021)
d.get_day()
d.get_month()
d.get_year()
d.tostring()
d.set_date(3,6,2022)
d.tostring()
d.set_day(18)
d.set_month(8)
d.set_year(2023)
d.tostring()



