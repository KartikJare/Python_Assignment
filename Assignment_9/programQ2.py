##########################################################
##
##  File name   : Assigment9Question2.py
##  Descreption : program which contains one function ChkGreater() that accepts two numbers
##                and prints the greater number.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 10 20
# Output: 20 is greater

def ChkGreater(No1,No2):
    
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    
    Ret = 0

    print("Enter First number : ")
    Value1 = int(input())

    print("Enter second number: ")
    Value2 = int(input())

    Ret = ChkGreater(Value1,Value2)

    print("Greater number : ",Ret)


if __name__ == "__main__":
    main()        