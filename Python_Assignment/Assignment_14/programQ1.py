##########################################################
##
##  File name   : Assigment14Question1.py
##  Descreption : lambda Accepts one number and returns square of that number
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Sqaure = lambda No : No * No


def main():
    Ret = 0

    print("Enter Number : ")
    Value = int(input())
    
    Ret = Sqaure(Value)

    print("Square number is : ",Ret)

if __name__ == "__main__":
    main()       