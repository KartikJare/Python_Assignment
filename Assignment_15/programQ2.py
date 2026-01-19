##########################################################
##
##  File name   : Assigment15Question2.py
##  Descreption : lambda Using filter() which accepts a list of 
##                numbers and returns a list of even Number
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def main():
    Data = [11,10,15,20,22,27,30]

    FData = list(filter((lambda No : No % 2 == 0),Data))
    
    print("Even Number are  : ",FData)

if __name__ == "__main__":
    main()       