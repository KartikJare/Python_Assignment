##########################################################
##
##  File name   : Assigment16Question10.py
##  Descreption : accept name from user and display length of its name
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def DislpayLenght(no):

    Count = 0
    for i in no:
        Count = Count + 1

    return Count   

def main():

    print("Enter Name: ")
    Name = input()

    Ret = DislpayLenght(Name)
    
    print(Ret)

if __name__ == "__main__":
    main()       