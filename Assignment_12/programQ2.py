##########################################################
##
##  File name   : Assigment12Question2.py
##  Descreption : Accepts one number and prints its factors
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

# Input: 12
# Output: 1 2 3 4 6 12

def Factors(No):
    i = 0

    for i in range(1,(No//2)+1):
        if(No % i == 0):
            print(i)    
    
    print(No)

def main():

    print("Enter number : ")
    Value1 = int(input())

    Factors(Value1)

if __name__ == "__main__":
    main()        