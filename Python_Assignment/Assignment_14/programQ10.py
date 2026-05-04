##########################################################
##
##  File name   : Assigment14Question10.py
##  Descreption : lambda Accepts three numbers and returns largest number
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Largest = lambda No1,No2,No3 : No1 if(No1 > No2 and No1 > No3) else (No2 if No2 > No3 else No3)  

def main():
    Ret = 0

    print("Enter frist Number : ")
    Value1 = int(input())

    print("Enter second Number : ")
    Value2 = int(input())

    print("Enter thrid Number : ")
    Value3 = int(input())

    Ret = Largest(Value1,Value2,Value3)
    
    print("Largest is : ",Ret)

if __name__ == "__main__":
    main()       