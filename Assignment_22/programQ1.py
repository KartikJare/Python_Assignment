##########################################################
##
##  File name   : Assigment22Question1.py
##  Descreption : Python program to implement a class named Demo
##  Author      : Kartik Ganesh Jare
##  Date        : 25/1/26
##
##########################################################

class Demo:
    
    Value = 10

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)
        print("Inside Fun")

    def Gun(self):
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)
        print("Inside Gun")

def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()    