##########################################################
##
##  File name   : Assigment21Question2.py
##  Descreption : creates creates two threads 
##                named Maximum element & Minimum element
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def Maximum(Arr):

    Max = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] > Max):
            Max = Arr[i]

    print("Maximum element in the list ",Max)
    print("End of Maximum Thread")      

def Min(Arr):

    Min = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] < Min):
            Min = Arr[i]

    print("Min element in the list ",Min)
    print("End of Maximum Thread")      


def main():
    
    Size = 0
    Value = 0

    print("Enter the number of Element: ")
    Size = int(input())

    Data = list()

    print("Enter the Elemnts :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)  
    
    tMax = threading.Thread(target=Maximum,args=(Data,))  
    tMin  = threading.Thread(target=Min,args=(Data,))   

    tMax.start()
    tMin.start()

    tMax.join()
    tMin.join()

    print("End of main")

if __name__ == "__main__":
    main();    