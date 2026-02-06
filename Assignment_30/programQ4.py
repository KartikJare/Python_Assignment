##########################################################
##
##  File name   : Assigment30Question4.py
##  Descreption : Copy File Contents into Another File
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts two file names from the user.
#   • First file is an existing file
#   • Second file is a new file
#   Copy all contents from the first file into the second file.
# Input:
#   ABC.txt Demo.txt
# Expected Output:
#   Contents of ABC.txt copied into Demo.txt.

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