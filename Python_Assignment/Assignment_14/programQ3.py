##########################################################
##
##  File name   : Assigment14Question3.py
##  Descreption : lambda Accepts two numbers and returns maximum number.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Maximum = lambda No1,No2 : No1 if No1 > No2 else No2 

def main():
    Ret = 0

    print("Enter frist Number : ")
    Value1 = int(input())

    print("Enter second Number : ")
    Value2 = int(input())
    
    Ret = Maximum(Value1,Value2)

    print("Maximum number is : ",Ret)

if __name__ == "__main__":
    main()       