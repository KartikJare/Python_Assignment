##########################################################
##
##  File name   : Assigment19Question4.py
##  Descreption : Accept contains filter(), map() and reduce()
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

# Filter Even number
# Map calculate square
# Reduce Addition  

from functools import reduce

def main():
    Size = 0
    Value = 0

    print("Enter the number of Element : ")
    Size = int(input())

    Data = list()

    print("Enter the Element : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)  

    print("Actual data is : ",Data)    

    FData = list(filter((lambda No :(No % 2 == 0)),Data))
    print("Data after filter is : ",FData)

    MData = list(map((lambda No : No ** 2),FData))
    print("Data after Map is : ",MData)

    RData = reduce((lambda A,B : A + B),MData)
    print("Data after reduce is : ",RData)
        
if __name__ ==  "__main__":
    main()   