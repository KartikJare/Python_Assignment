##########################################################
##
##  File name   : Assigment10Question1.py
##  Descreption : Accepts one number and prints multiplication table of that
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input : 4
# Output: 4 8 12 16 20 24 28 32 36 40

def Multiplication(No1):

    for i in range(1,11):
        print(No1 * i)

def main():

    print("Enter number : ")
    Value1 = int(input())

    Multiplication(Value1)

if __name__ == "__main__":
    main()        