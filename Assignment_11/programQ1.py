##########################################################
##
##  File name   : Assigment11Question1.py
##  Descreption : Accepts one number and checks whether it is prime or not
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 11
# Output: Prime Number

def ChkPrime(No):

    for i in range(2,No+1):
        if(No % i == 0):
            return True
        
def main():

    bRet = False

    print("Enter number : ")
    Value1 = int(input())

    bRet = ChkPrime(Value1)

    if(bRet == True):
        print("Is a prime Number")
    else:
        print("Is not a prime Number")   

if __name__ == "__main__":
    main()        