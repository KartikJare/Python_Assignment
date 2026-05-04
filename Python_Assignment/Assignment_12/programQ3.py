##########################################################
##
##  File name   : Assigment12Question3.py
##  Descreption : Accepts two numbers and prints addition, subtraction,multiplication and division.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def calculator(No1,No2):

    Ans = 0
    Ans = No1 + No2
    print("Addition  : ",Ans)

    Ans = 0
    Ans = No1 - No2
    print("subtraction : ",Ans)

    Ans = 0
    Ans = No1 * No2
    print("multiplication  : ",Ans)

    Ans = 0
    Ans = No1 // No2
    print("division  : ",Ans)

def main():

    print("Enter frist Number : ")
    Value1 = int(input())
    
    print("Enter second Number : ")
    Value2 = int(input())

    calculator(Value1,Value2)
   
if __name__ == "__main__":
    main()        