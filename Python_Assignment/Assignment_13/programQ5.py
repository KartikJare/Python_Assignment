##########################################################
##
##  File name   : Assigment13Question5.py
##  Descreption : Accepts marks and displays grade.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

# Condition Example:
# ≥ 75 → Distinction
# ≥ 60 → First Class
# ≥ 50 → Second Class
# < 50 → Fail

def DisplayGrade(No):

    if(No < 0 or No > 100):
        print("Please enter correct number")
        return

    if(No >= 75):
        print("Distinction")
    elif(No >= 60):    
        print("First Class")
    elif(No >= 50):
        print("Second Class") 
    else:
        print("Fail")    

def main():

    print("Enter number : ")
    Value1 = int(input())

    DisplayGrade(Value1)

if __name__ == "__main__":
    main()        