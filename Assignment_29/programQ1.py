##########################################################
##
##  File name   : Assigment29Question1.py
##  Descreption : Check File Exists in Current Directory
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts a file name from the user and checks whether that file exists in the current
#   directory or not.
# Input:
#   Demo.txt
# Expected Output:
#   Display whether Demo.txt exists or not.

import os

def main():
    FileName = input("Enter the name of file :")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("File is there in the directory")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()    
