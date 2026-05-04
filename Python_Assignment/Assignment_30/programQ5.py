##########################################################
##
##  File name   : Assigment30Question5.py
##  Descreption : Search a Word in File
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Problem Statement:
#   Write a program which accepts a file name and a word from the user and checks whether that word is present in
#   the file or not.
# Input:
#   Demo.txt Marvellous
# Expected Output:
#   Display whether the word Marvellous is found in Demo.txt or not.

def main():

    FileName = input("Enter the name of file :")
    Str = input("Enter a string to sreach :")

    try:
        fobj = open(FileName,"r")

        find = False

        for i in fobj:
            words = i.split()
            if(Str in words):
                find = True
                break

        if(find == True):
            print("Words is present in file")
        else:
            print("Words is not present in file")            
        
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    except PermissionError:
        print("File do not have permission to write")

if __name__ == "__main__":
    main()    
