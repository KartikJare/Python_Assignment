##########################################################
##
##  File name   : Assigment15Question8.py
##  Descreption : lambda Using filter() which accepts a list of numbers 
##                 and returns a list of numbers divisible by both 3 and 5
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def main():
    Data = [11,10,15,20,22,27,30]

    FData = list(filter((lambda No :(No % 3 == 0) and (No % 5 == 0)),Data))
    
    print("Divisible by both 3 and 5 : ",FData)

if __name__ == "__main__":
    main()       