##########################################################
##
##  File name   : Assigment16Question8.py
##  Descreption : Print * On screen 
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Dislpay(no):

    for i in range(no):
        print("*",end = " ")

def main():

    print("Enter a number :")
    Value = int(input())

    Dislpay(Value)

if __name__ == "__main__":
    main()       