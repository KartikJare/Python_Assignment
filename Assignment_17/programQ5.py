##########################################################
##
##  File name   : Assigment17Question5.py
##  Descreption : ChkPrime
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def ChkPrime(No):
   
    for i in range(2,No+1):
        if(No % i == 0):
            return True

def main():

    bRet = False

    print("Enter number : ")
    Value = int(input())

    bRet = ChkPrime(Value)

    if(bRet == True):
        print("Is a prime Number")
    else:
        print("Is not a prime Number")   

if __name__ == "__main__":
    main()       