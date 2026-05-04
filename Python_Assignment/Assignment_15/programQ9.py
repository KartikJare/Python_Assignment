##########################################################
##
##  File name   : Assigment15Question9.py
##  Descreption : lambda Using reduce() which accepts a list of numbers 
##                and returns the product of all Element
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]

    RData = reduce(lambda A,B: A * B,Data)
    
    print("Product of all element : ",RData)

if __name__ == "__main__":
    main()       