##########################################################
##
##  File name   : Assigment29Question2.py
##  Descreption : Display File Contents
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
#   console.
# Input:
#   Demo.txt
# Expected Output:
#   Display contents of Demo.txt on console.

def main():
    FileName = input("Enter the name of file :")

    try:
        fobj = open(FileName,"r")
        print("File gets succefully opened.")

        Data = fobj.read()

        print("Data from file is : ",Data)

        fobj.close()
    except FileNotFoundError:
        print("Unable to open file as there is no such file")


if __name__ == "__main__":
    main()    
