##########################################################
##
##  File name   : Assigment15Question10.py
##  Descreption : lambda Using filter() which accepts a list of numbers 
##                and returns the count of even number
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def main():
    Data = [11,10,15,20,22,27,30]

    FData = list(filter((lambda No :(No % 2 == 0)),Data))
    
    Count = len(FData)

    print("Even Count is  : ",Count)

if __name__ == "__main__":
    main()       