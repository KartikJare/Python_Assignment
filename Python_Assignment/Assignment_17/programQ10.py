##########################################################
##
##  File name   : Assigment17Question10.py
##  Descreption : Accept number from user and return number
##                addition of digits in that number.
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def AdditionDigit(No):

    Digit = 0
    iSum = 0

    while(No != 0):
        Digit = No %10
        iSum = Digit + iSum
        No = No // 10
    return iSum    

def main():

    print("Enter number : ")
    iValue = int(input())

    iRet = AdditionDigit(iValue)

    print("Addition of digit is : ",iRet)

if __name__ == "__main__":
    main()       