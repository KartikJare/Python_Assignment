##########################################################
##
##  File name   : Assigment29Question4.py
##  Descreption : Compare Two Files (Command Line)
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts two file names through command line arguments and compares the contents of
#   both files.
#   • If both files contain the same contents, display Success
#   • Otherwise display Failure
# Input (Command Line):
#   Demo.txt Hello.txt
# Expected Output:
#   Success OR Failureemo.txt.

import sys

def main():

    if(len(sys.argv) != 3):
        print("Ivalid Number of arguments")
        print("Please specify the name of dictory")
        return
    
    FileName = sys.argv[1]

    DestFile = sys.argv[2]

    try:
        fobj1 = open(FileName,"r")
        fobj2 = open(DestFile,"r")
        print("File gets succefully opened.")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")    
        
        fobj1.close()

        fobj2.close()        

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    except PermissionError:
        print("File do not have permission to write")
    
if __name__ == "__main__":
    main()    
