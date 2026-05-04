##########################################################
##
##  File name   : Assigment17Question9.py
##  Descreption : Accept number from user and return number
##                of digits in that number.
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def CountDigit(No):

    Digit = 0
    iCnt = 0

    while(No != 0):
        Digit = No %10
        No = No // 10
        iCnt = iCnt + 1
    return iCnt    

def main():

    print("Enter number : ")
    iValue = int(input())

    iRet = CountDigit(iValue)

    print("Digit count is : ",iRet)

if __name__ == "__main__":
    main()       