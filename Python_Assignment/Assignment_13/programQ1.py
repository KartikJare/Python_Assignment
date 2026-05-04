##########################################################
##
##  File name   : Assigment13Question1.py
##  Descreption : Accepts length and width of rectangle and prints area.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def Area(Value1,Value2):
    Area = 0

    Area = Value1 * Value2

    return Area
    
def main():
    Ret = 0

    print("Enter the Lenght of rectangle : ")
    No1 = int(input())

    print("Enter the width of rectangle : ")
    No2 = int(input())
    
    Ret = Area(No1,No2)

    print("Area is : ",Ret)

if __name__ == "__main__":
    main()       