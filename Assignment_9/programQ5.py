##########################################################
##
##  File name   : Assigment9Question5.py
##  Descreption : Accepts one number and checks whether it is divisible by 3 and 5
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##########################################################

# Input: 15
# Output : Divisible by 3 and 5

def Chkdivisible(No1):
    
    if(((No1 % 3) == 0) and ((No1 % 5) == 0)):
        return True
    else:
        return False 

def main():
    
    bRet = False

    print("Enter number : ")
    Value1 = int(input())

    Ret = Chkdivisible(Value1)
    
    if(Ret == True):
        print("Is Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()        