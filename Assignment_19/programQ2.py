##########################################################
##
##  File name   : Assigment19Question2.py
##  Descreption : Accept one lambda function 
##                and return multiplication.
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

Multiplication = lambda No1,No2 : No1 * No2

def main():
    value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the number: ")
    value1 = int(input())

    print("Enter the number: ")
    Value2 = int(input())

    Ret = Multiplication(value1,Value2)
    
    print("Multiplication is : ",Ret)    
        
if __name__ ==  "__main__":
    main()   