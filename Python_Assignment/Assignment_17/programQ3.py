##########################################################
##
##  File name   : Assigment17Question3.py
##  Descreption : Factorial
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact 

def main():
    
    Ret = 0

    print("Enter a number :")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()       