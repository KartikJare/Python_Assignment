##########################################################
##
##  File name   : Assigment15Question1.py
##  Descreption : lambda Using map() which accepts a list of 
##                numbers and returns a list of squares of
##                each number.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def main():
    Data = [11,10,15,20,22,27,30]

    MData = list(map((lambda No : No * No),Data))
    
    print("Square number are : ",MData)

if __name__ == "__main__":
    main()       