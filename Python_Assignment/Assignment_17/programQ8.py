##########################################################
##
##  File name   : Assigment17Question8.py
##  Descreption : Accept one number and display pattern
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def Display(No):

    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end="\t")
        print()       

def main():

    print("Enter number :")
    Value = int(input())
    
    Display(Value)

if __name__ == "__main__":
    main()       