##########################################################
##
##  File name   : Assigment9Question3.py
##  Descreption : Accepts one number and prints square of that number
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 5
# Output : 25

def ChkSquare(No1):
    return No1 * No1

def main():
    
    Ret = 0

    print("Enter number : ")
    Value1 = int(input())

    Ret = ChkSquare(Value1)

    print("Sauare root is : ",Ret)

if __name__ == "__main__":
    main()        