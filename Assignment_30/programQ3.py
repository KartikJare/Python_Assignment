##########################################################
##
##  File name   : Assigment30Question3.py
##  Descreption : Display File Line by Linee
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts a file name from the user and displays the contents of the file line by line on the
#   screen.
# Input:
#   Demo.txt
# Expected Output:
#   Display each line of Demo.txt one by one.

def main():
    FileName = input("Enter the name of file :")

    try:
        fobj = open(FileName,"r")
        print("File gets succefully opened.")
      
        for i in fobj:
            print(i,end="")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

if __name__ == "__main__":
    main()    
