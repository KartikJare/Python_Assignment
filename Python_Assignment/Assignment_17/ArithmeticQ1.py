##########################################################
##
##  File name   : Assigment17Question1.py
##  Descreption : Create a module of Arithmetic 
##                doing add,div,mult and subtraction 
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Sub(No1,No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def Div(No1,No2):
    Ans = 0
    Ans = No1 / No2
    if(Ans == 0):
        print("Division by zero is not possible")
    return Ans

def Mult(No1,No2):
    Ans = 0
    Ans = No1 * No2
    return Ans