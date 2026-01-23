##########################################################
##
##  File name   : Assigment20Question4.py
##  Descreption : creates 3 separate threads named 
##                Small thread should count and display the number of lowercase characters.
##                Capital thread should count and display the number of uppercase characters.
##                Digits thread should count and display the number of numeric digits.
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import threading

def CountSmall(str):
    iCount = 0

    for ch in str:
        if((ch >= 'a') and (ch <= 'z')):
            iCount += 1

    print("Count Small Thread id : ",threading.get_ident())
    print("Number of Small letter : ",iCount)
    print("End of Small count thread");         

def CountCapital(str):
    iCount = 0

    for ch in str:
        if((ch >= 'A') and (ch <= 'Z')):
            iCount += 1

    print("Count Capital Thread id : ",threading.get_ident())
    print("Number of Capital letter : ",iCount)
    print("End of Capital count thread") 

def CountDigit(str):
    iCount = 0

    for ch in str:
        if((ch >= '0') and (ch <= '9')):
            iCount += 1

    print("Count Digit Thread id : ",threading.get_ident())
    print("Digit are : ",iCount)
    print("End of Digit count thread")

def main():
    Value = 0

    print("Enter the string : ")
    Value = input()

    tSmall = threading.Thread(target=CountSmall,args=(Value,))  
    tCaptial  = threading.Thread(target=CountCapital,args=(Value,))   
    tdigit = threading.Thread(target=CountDigit,args=(Value,))   

    tSmall.start()
    tCaptial.start()
    tdigit.start()

    tSmall.join()
    tCaptial.join()
    tdigit.join()

    print("End of main")

if __name__ == "__main__":
    main();    