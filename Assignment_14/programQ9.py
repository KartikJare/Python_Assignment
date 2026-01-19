##########################################################
##
##  File name   : Assigment14Question9.py
##  Descreption : lambda Accepts two numbers and returns multiplication
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Multiplication= lambda No1,No2 : No1 * No2

def main():
    Ret = 0

    print("Enter frist Number : ")
    Value1 = int(input())

    print("Entersecond Number : ")
    Value2 = int(input())

    Ret = Multiplication(Value1,Value2)
    
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()       