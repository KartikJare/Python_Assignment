##########################################################
##
##  File name   : Assigment20Question2.py
##  Descreption : creates two separate threads named 
##                EvenFactor and OddFactor
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def EvenSumFactor(No):
    sum = 0
    DataEven = list()

    for i in range(1,No+1):
        if((No % i == 0) and (i % 2 == 0)):
            DataEven.append(i)
            sum += i

    print("Sum is ",sum)
    print("End of Even Factor thread")

def OddSumFactor(No):
    sum = 0
    DataOdd = list()

    for i in range(1,No+1):
        if((No % i == 0) and (i % 2 != 0)):
            DataOdd.append(i)
            sum += i

    print("Sum is ",sum)
    print("End of Even Factor thread")


def main():

    print("Enter a number : ")
    Value = int(input())
    
    tEven = threading.Thread(target=EvenSumFactor,args=(Value,))  
    todd  = threading.Thread(target=OddSumFactor,args=(Value,))   

    tEven.start()
    todd.start()

    tEven.join()
    todd.join()

    print("End of main")

if __name__ == "__main__":
    main();    