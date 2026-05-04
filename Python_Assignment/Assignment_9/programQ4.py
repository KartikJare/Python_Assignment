##########################################################
##
##  File name   : Assigment9Question4.py
##  Descreption : Accepts one number and prints cube of that number.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 5
# Output : 25

def ChkCube(No1):
    return No1 * No1* No1

def main():
    
    Ret = 0

    print("Enter number : ")
    Value1 = int(input())

    Ret = ChkCube(Value1)

    print("Cude is : ",Ret)

if __name__ == "__main__":
    main()        