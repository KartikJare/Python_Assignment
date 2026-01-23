##########################################################
##
##  File name   : Assigment20Question5.py
##  Descreption : creates two separate threads named 
##                Thread1 - 1 to 50, Thread2 - 50 -1
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def NumberOrder():

    for i in range(1,51):
        print("Number in Order : ",i)

    print("Number Order Thread finished")

def NumberReverse():

    for i in range(50,0,-1):
        print("Number in Reverse : ",i)

    print("Number Reverse Thread finished")

def main():
    
    torder = threading.Thread(target=NumberOrder)  
    treverse  = threading.Thread(target=NumberReverse)   

    torder.start()

    torder.join()

    treverse.start()

    treverse.join()

    print("End of main")

if __name__ == "__main__":
    main();    