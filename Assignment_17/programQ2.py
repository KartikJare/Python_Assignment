##########################################################
##
##  File name   : Assigment17Question2.py
##  Descreption : Accept one number and display pattern
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Display(No):

    for i in range(No):
        for j in range(No):
            print("*",end="\t")
        print()       

def main():

    print("Enter number :")
    Value = int(input())
    
    Display(Value)

if __name__ == "__main__":
    main()       