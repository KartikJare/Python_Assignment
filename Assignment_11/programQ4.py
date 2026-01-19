##########################################################
##
##  File name   : Assigment11Question4.py
##  Descreption : Accepts one number and prints reverse of that number.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 123
# Output: 321

def Reverse(No):
   
    Digit = 0
    Rev = 0

    while(No != 0):
       Digit = No % 10
       Rev  = Rev * 10 + Digit
       No = No // 10 

    return Rev    

def main():

    Ret = 0

    print("Enter number : ")
    Value1 = int(input())

    Ret = Reverse(Value1)

    print("Reverse number is : ",Ret)

if __name__ == "__main__":
    main()        