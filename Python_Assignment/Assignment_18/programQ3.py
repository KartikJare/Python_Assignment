##########################################################
##
##  File name   : Assigment18Question3.py
##  Descreption : Accept N number and return Minimum
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Minimum(Arr):

    Min = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] < Min):
            Min = Arr[i]

    return Min         

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
    
    Ret = Minimum(Data)
    
    print("Minimum is : ",Ret)    
        
if __name__ ==  "__main__":
    main()   