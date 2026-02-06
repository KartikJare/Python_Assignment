##########################################################
##
##  File name   : Assigment31Question1.py
##  Descreption : Design automation script which accept directory name
##                and file extension from user. Display all files with that extension.
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.

import sys
from programfilesreachmoduleQ1 import Filevaild,serachFile

def main():

    if len(sys.argv) != 3:
        print("Invaild agrument entry")
        return

    DirName = sys.argv[1]
    Extension = sys.argv[2]

    if (Filevaild != DirName):
        print("Directory does not exits")
        return

    Ret = serachFile(DirName,Extension)

    if len(Ret) == 0:
        print(f"File not found with extension {Extension}")
    else:
        print(f"File with extension {Extension}")
        for i in Ret:
            print(i)

if __name__ == "__main__":
    main()    