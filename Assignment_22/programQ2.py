##########################################################
##
##  File name   : Assigment22Question2.py
##  Descreption : Python program to implement a class named cricle
##  Author      : Kartik Ganesh Jare
##  Date        : 25/1/26
##
##########################################################

class Cricle:
    
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accpet(self):
        self.Radius = float(input("Enter the radius of the cricle :  "))

    def CalculateArea(self):
        self.Area = Cricle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Cricle.PI * self.Radius 

    def Display(self):
        print("Radius :",self.Radius)
        print("Area :",self.Area)           
        print("Circumference :",self.Circumference)


def main():
    obj1 = Cricle()
    obj1.Accpet()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2 = Cricle()
    obj2.Accpet()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__ == "__main__":
    main()    