##########################################################
##
##  File name   : Assigment20Question1.py
##  Descreption : creates two separate threads named Even and Odd
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def DisplayEven():

    for i in range(2,21,2):
        print("Even : ",i)

    print("Even Thread finished")

def DisplayOdd():

    for i in range(1,20,2):
        print("odd : ",i)

    print("Odd Thread finished")

def main():
    
    tEven = threading.Thread(target=DisplayEven)  
    todd  = threading.Thread(target=DisplayOdd)   

    tEven.start()
    todd.start()

    tEven.join()
    todd.join()

    print("End of main")

if __name__ == "__main__":
    main();    