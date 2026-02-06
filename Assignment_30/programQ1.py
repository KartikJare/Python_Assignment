##########################################################
##
##  File name   : Assigment30Question1.py
##  Descreption : Count Lines in a File
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
#   Demo.txt
# Expected Output:
#   Total number of lines in Demo.txt.

import os

def main():
    FileName = input("Enter the name of file :")

    try:
        fobj = open(FileName,"r")
        print("File gets succefully opened.")

        lineCount = 0

        for i in fobj:
            lineCount = lineCount + 1

        print("Line in the file are : ",lineCount)

        fobj.close()
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

if __name__ == "__main__":
    main()    
