##########################################################
##
##  File name   : Assigment19Question3.py
##  Descreption : Accept contains filter(), map() and reduce()
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

#Filter greater than or equal to 70 and less than or equal to 90 
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers  

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

    FData = list(filter((lambda No :(No >= 70 and  No <= 90)),Data))
    print("Data after filter is : ",FData)

    MData = list(map((lambda No : No + 10),FData))
    print("Data after Map is : ",MData)

    RData = reduce((lambda A,B : A * B),MData)
    print("Data after reduce is : ",RData)
        
if __name__ ==  "__main__":
    main()   