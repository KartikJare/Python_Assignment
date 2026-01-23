##########################################################
##
##  File name   : Assigment16Question3.py
##  Descreption : Add ()
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Add(no1,no2):
    
    Ans = 0
    
    Ans = no1 + no2

    return Ans

def main():
    
    Ret = 0

    print("Enter a number :")
    Value1 = int(input())

    print("Enter a number :")
    Value2 = int(input())
    
    Ret = Add(Value1,Value2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()       