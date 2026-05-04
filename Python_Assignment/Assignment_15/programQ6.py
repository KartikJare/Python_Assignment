##########################################################
##
##  File name   : Assigment15Question6.py
##  Descreption : lambdaUsing reduce() which accepts a list of numbers 
##                and returns the minimum element
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]

    RData = reduce((lambda A,B: A if A < B else B),Data)
    
    print("Minimum is  : ",RData)

if __name__ == "__main__":
    main()       