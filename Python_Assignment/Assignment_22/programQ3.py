##########################################################
##
##  File name   : Assigment22Question3.py
##  Descreption : Python program to implement a class named Arithmetic
##  Author      : Kartik Ganesh Jare
##  Date        : 25/1/26
##
##########################################################

class Arithematic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter frist number :"))
        self.value2 = int(input("Enter frist number :"))

    def Addition(self):
        Ans = 0
        Ans = self.value1 + self.value2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.value1 - self.value2
        return Ans
    
    def Multiplication(self):
        Ans = 0
        Ans = self.value1 * self.value2
        return Ans
    
    def Division(self):
        Ans = 0
        Ans = self.value1 / self.value2
        return Ans

def main():

    obj1 = Arithematic()
    obj1.Accept()
    print("Addition is  : ",obj1.Addition())
    print("Substraction is  : ",obj1.Substraction())
    print("Multiplication is  : ",obj1.Multiplication())
    print("Division is  : ",obj1.Division())

if __name__ == "__main__":
    main()    