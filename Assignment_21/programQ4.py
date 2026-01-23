##########################################################
##
##  File name   : Assigment21Question4.py
##  Descreption : Create 2 Thread 
##                1 Thread sum and 2 thread product  
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def Summtation(Arr):

    iSum = 0

    for i in range(len(Arr)):
        iSum = iSum + Arr[i]

    print("Sum of element in the list ",iSum)
    print("End of Summtation Thread")      

def Product(Arr):

    iSum = 1

    for i in range(len(Arr)):
        iSum = iSum * Arr[i]

    print("Product of element in the list ",iSum)
    print("End of Product Thread")

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
    
    tsum = threading.Thread(target=Summtation,args=(Data,))  
    tproduct  = threading.Thread(target=Product,args=(Data,))   

    tsum.start()
    tproduct.start()

    tsum.join()
    tproduct.join()

    print("End of main")

if __name__ == "__main__":
    main();    