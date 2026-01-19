##########################################################
##
##  File name   : Assigment12Question4.py
##  Descreption : Accepts one number and prints that many numbers starting
##                from 1
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

# Input: 5
# Output: 1 2 3 4

def Count(No):

    for i in range(1,No):
        print(i)    

def main():

    print("Enter number : ")
    Value1 = int(input())

    Count(Value1)

if __name__ == "__main__":
    main()        