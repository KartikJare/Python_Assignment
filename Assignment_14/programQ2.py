##########################################################
##
##  File name   : Assigment14Question2.py
##  Descreption : lambda Accepts one number and returns cube of that number.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

Cude = lambda No : No * No * No

def main():
    Ret = 0

    print("Enter Number : ")
    Value = int(input())
    
    Ret = Cude(Value)

    print("Cude number is : ",Ret)

if __name__ == "__main__":
    main()       