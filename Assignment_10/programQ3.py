##########################################################
##
##  File name   : Assigment10Question3.py
##  Descreption : Accepts one number and prints factorial of that number
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 5
# Output: 120

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    print("Enter number : ")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()