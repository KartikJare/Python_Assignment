##########################################################
##
##  File name   : Assigment11Question3.py
##  Descreption : Accepts one number and prints sum of digits.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 123
# Output: 6

def CountSumDigit(No):
   
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum    

def main():

    Ret = 0

    print("Enter number : ")
    Value1 = int(input())

    Ret = CountSumDigit(Value1)

    print("Number of Digits are : ",Ret)

if __name__ == "__main__":
    main()        