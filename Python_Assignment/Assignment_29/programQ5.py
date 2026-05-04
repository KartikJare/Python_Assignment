##########################################################
##
##  File name   : Assigment29Question5.py
##  Descreption : Frequency of a String in File
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts a file name and one string from the user and returns the frequency (count of
#   occurrences) of that string in the file.
# Input:
#   Demo.txt Marvellous
# Expected Output:
#   Count how many times "Marvellous" appears in Demo.txt.


def main():

    FileName = input("Enter the name of file :")
    Str = input("Enter a string to sreach :")

    try:
        fobj = open(FileName,"r")

        Data = fobj.read()

        Count = Data.count(Str)
    
        print(f"Frequency of {Str} in {FileName} is : {Count}")

        fobj.close
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    except PermissionError:
        print("File do not have permission to write")

if __name__ == "__main__":
    main()    
