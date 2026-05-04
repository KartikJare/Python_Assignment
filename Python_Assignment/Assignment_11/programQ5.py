##########################################################
##
##  File name   : Assigment11Question5.py
##  Descreption : Accepts one number and checks whether it is palindrome or not
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 121
# Output: Palindrome

def Palindrome(No):
   
    Digit = 0
    Rev = 0
    Temp = No

    while(No != 0):
       Digit = No % 10
       Rev  = Rev * 10 + Digit
       No = No // 10 

    if(Temp == Rev):
        return True
    else:
        return False    

def main():

    bRet = False

    print("Enter number : ")
    Value1 = int(input())

    bRet = Palindrome(Value1)

    if(bRet == True):
        print("Is a Palindrome")
    else:
        print("Is not a Palindrome")           

if __name__ == "__main__":
    main()        