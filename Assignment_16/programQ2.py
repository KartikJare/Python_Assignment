##########################################################
##
##  File name   : Assigment16Question2.py
##  Descreption : Check Even or odd
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def ChkNum(no):

    if(no % 2 == 0):
        return  True
    else:
        return False

def main():
    
    bRet = False

    print("Enter a number :")
    Value = int(input())

    bRet = ChkNum(Value)

    if(bRet == True):
        print("The number is even")
    else:
        print("The number is odd")

if __name__ == "__main__":
    main()       