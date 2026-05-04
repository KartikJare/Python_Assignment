##########################################################
##
##  File name   : Assigment10Question4.py
##  Descreption : Accepts one number and prints all even numbers 
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 10
# Output: 2 4 6 8 10

def Even(No):

    for i in range(1,No+1):
        if((i % 2) == 0):
            print(i)

def main():
    
    print("Enter number : ")
    Value = int(input())
    
    Even(Value)


if __name__ == "__main__":
    main()