##########################################################
##
##  File name   : Assigment14Question7.py
##  Descreption : lambda Accepts one number and returns True if divisible by 5.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

ChkDivisible  = lambda No : (No % 5 == 0)

def main():
    Ret = 0

    print("Enter Number : ")
    Value1 = int(input())

    Ret = ChkDivisible(Value1)
    
    if(Ret == True):
        print("It is Divisible 5")
    else:
        print("It is not Divisible 5")

if __name__ == "__main__":
    main()       