##########################################################
##
##  File name   : Assigment13Question2.py
##  Descreption : Accepts radius of circle and prints area of circle
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def Area(Radius):
    
    Area = 0.0
    PI = 3.14

    Area = PI * Radius * Radius

    return Area
    
def main():
    Ret = 0

    print("Enter radius of circle : ")
    No = float(input()) 
    
    Ret = Area(No)  

    print("Area of cricle is : ",Ret)

if __name__ == "__main__":
    main()    