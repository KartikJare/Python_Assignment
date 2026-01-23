##########################################################
##
##  File name   : Assigment19Question1.py
##  Descreption : Accept one lambda function and return power of 2
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

Power = lambda No : 2 ** No

def main():
    value = 0
    Ret = 0

    print("Enter the number: ")
    value = int(input())

    Ret = Power(value)
    
    print("Result is : ",Ret)    
        
if __name__ ==  "__main__":
    main()   