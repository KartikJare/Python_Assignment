##########################################################
##
##  File name   : Assigment23Question3.py
##  Descreption : Python program to implement a class named Number
##  Author      : Kartik Ganesh Jare
##  Date        : 25/1/26
##
##########################################################

class Number:

    def __init__(self):
        self.Value = 0

    def Accept(self):
        self.Value = int(input("Enter a number :"))

    def ChkPrime(self):

        for i in range(2,self.Value):
            if(self.Value % i ==0):
                return False
        return True    

    def ChkPerfect(self):
        
        sum = 0

        for i in range(1,(self.Value // 2)+1):
            if(self.Value % i == 0):
                sum = sum + i

        if(sum == self.Value):
            return True
        else:
            return False
    
    def Factor(self):

        print("Factors are : ")
        for i in range(1,(self.Value)+1):
            if(self.Value % i == 0):
                print(i)
    
    def SumFactor(self):

        sum = 0

        for i in range(1,(self.Value)+1):
            if(self.Value % i == 0):
                sum = sum + i

        return sum

def main():

    obj1 = Number()
    obj1.Accept()

    print("Prime Number are : ",obj1.ChkPrime())
    obj1.Factor()
    print("Sum of Factors are : ",obj1.SumFactor())
    print("Perfect are : ",obj1.ChkPerfect())
    
if __name__ == "__main__":
    main()    