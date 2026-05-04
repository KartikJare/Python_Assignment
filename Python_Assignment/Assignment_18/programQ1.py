##########################################################
##
##  File name   : Assigment18Question1.py
##  Descreption : Accept N number and return Addition
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Summation(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
        
    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of Element: ")
    Size = int(input())

    Data = list()

    print("Enter the Elemnts :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)  
    
    Ret = Summation(Data)
    
    print("Summation is : ",Ret)    
        
if __name__ ==  "__main__":
    main()   