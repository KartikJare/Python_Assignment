##########################################################
##
##  File name   : Assigment13Question3.py
##  Descreption : Accepts one number and checks whether it is perfect number or not
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

# Input: 6
# Output: Perfect Number

def ChkPerfect(No):

    Sum = 0

    for i in range(1,(No // 2)+1):
        if(No % i == 0):
            Sum = Sum + i

    if(Sum == No):
        return True
    else:
        return False    

def main():

    bRet = False

    print("Enter Number : ")
    Value1 = int(input())

    bRet = ChkPerfect(Value1)

    if(bRet == True):
        print("Number is a precfet Number")
    else:
        print("Number is  Not a precfet Number")            

if __name__ == "__main__":
    main()        