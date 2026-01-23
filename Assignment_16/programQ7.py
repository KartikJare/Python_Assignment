##########################################################
##
##  File name   : Assigment16Question7.py
##  Descreption : Check diviside by 5 
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def ChkDivisible(no):

    if(no % 5 == 0):
        return  True
    else:
        return False

def main():
    
    bRet = False

    print("Enter a number :")
    Value = int(input())

    bRet = ChkDivisible(Value)

    if(bRet == True):
        print("The number is Divisible by 5")
    else:
        print("The number is not Divisible by 5")

if __name__ == "__main__":
    main()       