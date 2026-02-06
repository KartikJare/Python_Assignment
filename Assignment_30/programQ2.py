##########################################################
##
##  File name   : Assigment30Question2.py
##  Descreption : Count Words in a File
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
#   Demo.txt
# Expected Output:
#   Total number of words in Demo.txt.

def main():
    FileName = input("Enter the name of file :")

    try:
        fobj = open(FileName,"r")
        print("File gets succefully opened.")

        count = 0
      
        for i in fobj:
            words = i.split()
            count = count + len(words)
            
        print("Number of word in file : ",count)

        fobj.close()
    except FileNotFoundError:
        print("Unable to open file as there is no such file")


if __name__ == "__main__":
    main()    
