##########################################################
##
##  File name   : Assigment18Question5.py
##  Descreption : Accept N number and return 
##                frequency of that number from List
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import MarvellousNumQ5

def SumPrime(Arr):

    Sum = 0

    for i in range(len(Arr)):
        if(MarvellousNumQ5.ChkPrime(Arr[i])):
            Sum = Sum + Arr[i]

    return Sum        

def main():
    Size = 0
    Value1 = 0
    Ret = 0

    print("Enter the number of Element: ")
    Size = int(input())

    Data = list()

    print("Enter the Elemnts :")

    for i in range(Size):
        Value1 = int(input())
        Data.append(Value1)  

    Ret = SumPrime(Data)
    
    print("Summation is of prime number : ",Ret)    
        
if __name__ ==  "__main__":
    main()   