##########################################################
##
##  File name   : Assigment12Question5.py
##  Descreption : Accepts one number and prints that many numbers in reverse order
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

# Input: 5
# Output: 5 4 3 2 1

def Count(No):

    for i in range(No,0,-1):
        print(i)    

def main():

    print("Enter number : ")
    Value1 = int(input())

    Count(Value1)

if __name__ == "__main__":
    main()        