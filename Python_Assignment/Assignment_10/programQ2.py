##########################################################
##
##  File name   : Assigment10Question2.py
##  Descreption : Accepts one number and prints sum of first N natural numbers
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 5
# Output: 15

def ChkNatural(No):
    
    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + i

    return Sum    

def main():

    Ret = 0

    print("Enter number : ")
    Value1 = int(input())

    Ret = ChkNatural(Value1)

    print("Natural number is : ",Ret)

if __name__ == "__main__":
    main()        