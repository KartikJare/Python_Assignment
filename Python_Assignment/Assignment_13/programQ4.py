##########################################################
##
##  File name   : Assigment13Question4.py
##  Descreption : Accepts one number and prints binary equivalent
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def DisplayBinary(No):

    Binary = ""

    while(No > 0):
        Digit = No % 2
        Binary = str(Digit) + Binary
        No = No // 2 

    print(Binary)

def main():
    
    print("Enter Number : ")
    Value = int(input())

    DisplayBinary(Value)

if __name__ == "__main__":
    main()        