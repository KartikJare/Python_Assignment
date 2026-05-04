##########################################################
##
##  File name   : Assigment14Question5.py
##  Descreption : lambda accepts one number and returns True if number is even
##                 otherwise False.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Even = lambda No : (No % 2 == 0)

def main():
    Ret = 0

    print("Enter Number : ")
    Value1 = int(input())

    Ret = Even(Value1)
    
    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")

if __name__ == "__main__":
    main()       