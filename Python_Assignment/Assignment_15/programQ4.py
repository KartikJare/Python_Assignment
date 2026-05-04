##########################################################
##
##  File name   : Assigment15Question4.py
##  Descreption : lambda using reduce() which accepts a list of numbers 
##                and returns the addition of all element
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]

    RData = reduce((lambda A,B : A + B),Data)
    
    print("Addition is  : ",RData)

if __name__ == "__main__":
    main()       