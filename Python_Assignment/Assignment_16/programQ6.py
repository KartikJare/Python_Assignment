##########################################################
##
##  File name   : Assigment16Question6.py
##  Descreption : Check number whether is positive or negative or zero
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def ChkNum(No):

    if(No > 0):
        print("Positive number")
    elif(No < 0):
        print("Negative Number")
    elif(No == 0):
        print("Zero")

def main():

    print("Enter a number :")
    Value = int(input())

    ChkNum(Value)

if __name__ == "__main__":
    main()                       

