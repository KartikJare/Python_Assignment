##########################################################
##
##  File name   : Assigment17Question1.py
##  Descreption : Create a module of Arithmetic 
##                doing add,div,mult and subtraction
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

import ArithmeticQ1

def main():
   
   Ret  = 0

   print("Enter the First Number : ")
   Value1 = int(input())

   print("Enter the second Number : ")
   Value2 = int(input())

   Ret = ArithmeticQ1.Add(Value1,Value2)
   print("Addition is : ",Ret)

   Ret = ArithmeticQ1.Sub(Value1,Value2)
   print("Subtraction is : ",Ret)

   Ret = ArithmeticQ1.Div(Value1,Value2)
   print("Division is : ",Ret)

   Ret = ArithmeticQ1.Mult(Value1,Value2)
   print("Multiplication is : ",Ret)



if __name__ == "__main__":
    main()       