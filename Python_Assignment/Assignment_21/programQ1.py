##########################################################
##
##  File name   : Assigment21Question1.py
##  Descreption : creates creates two threads 
##                named Prime and NonPrime.
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def DisplayPrime(Arr):

    for no in Arr:
        bFlag = True
        for i in range(2,no):
            if(no % i == 0):
                bFlag = False
                break
        if bFlag:
            print("prime number are : ",no)
    
    print("End of Prime Thread")

def DisplayNonPrime(Arr):

    for no in Arr:
        bFlag = True
        for i in range(2,no):
            if(no % i == 0):
                bFlag = False
                break
        if not bFlag:    
            print("Nonprime number are : ",no)
    
    print("End of NonPrime Thread")

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
    
    tPrime = threading.Thread(target=DisplayPrime,args=(Data,))  
    tNonPrime  = threading.Thread(target=DisplayNonPrime,args=(Data,))   

    tPrime.start()
    tNonPrime.start()

    tPrime.join()
    tNonPrime.join()

    print("End of main")

if __name__ == "__main__":
    main();    