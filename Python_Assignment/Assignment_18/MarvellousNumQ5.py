##########################################################
##
##  File name   : Assigment18Question5.py
##  Descreption : Accept N number and return 
##                frequency of that number from List
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def ChkPrime(No):

    for i in range(2,No):
        if(No % i == 0):
            return False

    return True    