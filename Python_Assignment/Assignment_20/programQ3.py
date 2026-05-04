##########################################################
##
##  File name   : Assigment20Question3.py
##  Descreption : creates two separate threads named 
##                Evenlist and Oddlist and display and sum it
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def EvenSum(Arr):
    sum = 0
    DataEven = list()

    for i in Arr:
        if(i % 2 == 0):
            DataEven.append(i)
            sum += i
    
    print("Even is ",DataEven)
    print("Sum is ",sum)
    print("End of Even thread")

def OddSum(Arr):
    sum = 0
    DataOdd = list()

    for i in Arr:
        if(i % 2 != 0):
            DataOdd.append(i)
            sum += i
    
    print("Odd is ",DataOdd)
    print("Sum is ",sum)
    print("End of Odd thread")

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
    
    tEven = threading.Thread(target=EvenSum,args=(Data,))  
    todd  = threading.Thread(target=OddSum,args=(Data,))   

    tEven.start()
    todd.start()

    tEven.join()
    todd.join()

    print("End of main")

if __name__ == "__main__":
    main();    