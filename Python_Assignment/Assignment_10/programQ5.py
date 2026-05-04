##########################################################
##
##  File name   : Assigment10Question5.py
##  Descreption : Accepts one number and prints all odd numbers 
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

def odd(No):

    for i in range(1,No+1):
        if((i % 2) != 0):
            print(i)

def main():
    
    print("Enter number : ")
    Value = int(input())
    
    odd(Value)


if __name__ == "__main__":
    main()