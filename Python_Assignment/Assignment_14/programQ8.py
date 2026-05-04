##########################################################
##
##  File name   : Assigment14Question8.py
##  Descreption : lambda Accepts two numbers and returns addition.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Addition = lambda No1,No2 : No1 + No2

def main():
    Ret = 0

    print("Enter frist Number : ")
    Value1 = int(input())

    print("Entersecond Number : ")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)
    
    print("addition is : ",Ret)

if __name__ == "__main__":
    main()       