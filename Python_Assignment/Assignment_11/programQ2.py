##########################################################
##
##  File name   : Assigment11Question2.py
##  Descreption : Accepts one number and prints count of digits in that number.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 7521
# Output: 4

def CountDigit(No):
    
    i = 0

    while(No != 0):
        No = No // 10
        i = i + 1

    return i    

def main():

    Ret = 0

    print("Enter number : ")
    Value1 = int(input())

    Ret = CountDigit(Value1)

    print("Number of Digits are : ",Ret)

if __name__ == "__main__":
    main()        