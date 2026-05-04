##########################################################
##
##  File name   : Assigment17Question4.py
##  Descreption : factors Sum
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def SumFactor(No):
    sum = 0

    for i in range(1,(No//2)+1):
        if(No % i == 0):
            sum += i

    return sum 

def main():

    Ret = 0

    print("Enter a number :")
    Value = int(input())

    Ret = SumFactor(Value)

    print("Summation of Factor is : ",Ret)

if __name__ == "__main__":
    main()       