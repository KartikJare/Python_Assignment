##########################################################
##
##  File name   : Assigment18Question4.py
##  Descreption : Accept N number and return 
##                frequency of that number from List
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def ChkFrequency(Arr,No):

    iCount = 0

    for i in range(len(Arr)):
        if(Arr[i] == No):
            iCount += 1
            
    return iCount         

def main():
    Size = 0
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the number of Element: ")
    Size = int(input())

    Data = list()

    print("Enter the Elemnts :")

    for i in range(Size):
        Value1 = int(input())
        Data.append(Value1)  
    
    print("Enter number which your want to sreach :")
    Value2 = int(input())

    Ret = ChkFrequency(Data,Value2)
    
    print(f"Frequency of {Value2} is : {Ret}")    
        
if __name__ ==  "__main__":
    main()   