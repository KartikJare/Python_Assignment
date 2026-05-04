##########################################################
##
##  File name   : Assigment29Question3.py
##  Descreption : Copy File Contents into a New File (Command Line)
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts an existing file name through command line arguments, creates a new file
#   named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line):
#   ABC.txt
# Expected Output:
#   Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys

def main():

    if(len(sys.argv) != 3):
        print("Ivalid Number of arguments")
        print("Please specify the name of dictory")
        return
    
    FileName = sys.argv[1]

    DestFile = sys.argv[2]

    try:
        fobj = open(FileName,"r")
        print("File gets succefully opened.")

        Data = fobj.read()

        dobj = open(DestFile,"w")

        Wdest = dobj.write(Data)

        print(f"Data of {FileName} copied successfully into {DestFile}")

        fobj.close()

        dobj.close()        

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    except PermissionError:
        print("File do not have permission to write")
    


if __name__ == "__main__":
    main()    
