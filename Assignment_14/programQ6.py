##########################################################
##
##  File name   : Assigment14Question6.py
##  Descreption : lambda accepts one number and returns True if number is odd
##                 otherwise False.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Odd = lambda No : (No % 2 != 0)

def main():
    Ret = 0

    print("Enter Number : ")
    Value1 = int(input())

    Ret = Odd(Value1)
    
    if(Ret == True):
        print("It is Odd")
    else:
        print("It is Even")

if __name__ == "__main__":
    main()       