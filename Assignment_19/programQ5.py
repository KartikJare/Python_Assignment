##########################################################
##
##  File name   : Assigment19Question5.py
##  Descreption : Accept contains filter(), map() and reduce()
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

# Filter prime number
# Map multiply by 2
# Reduce will return Maximum number from that numbers

from functools import reduce

def Prime(No):
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True
    
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

    FData = list(filter(Prime,Data))
    print("Data after filter is : ",FData)

    MData = list(map((lambda No : No * 2),FData))
    print("Data after Map is : ",MData)

    RData = reduce((lambda A,B : A if A > B else B),MData)
    print("Data after reduce is : ",RData)
        
if __name__ ==  "__main__":
    main()   