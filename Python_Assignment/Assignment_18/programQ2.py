##########################################################
##
##  File name   : Assigment18Question2.py
##  Descreption : Accept N number and return Maximum
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Maximum(Arr):

    Max = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] > Max):
            Max = Arr[i]

    return Max         

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
    
    Ret = Maximum(Data)
    
    print("Maximum is : ",Ret)    
        
if __name__ ==  "__main__":
    main()   