##########################################################
##
##  File name   : Assigment16Question5.py
##  Descreption : Display 10 to 1 on screen
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Dislpay(no):

    for i in range(no,0,-1):
        print(i)

def main():

    print("Enter a number :")
    Value = int(input())

    Dislpay(Value)

if __name__ == "__main__":
    main()       