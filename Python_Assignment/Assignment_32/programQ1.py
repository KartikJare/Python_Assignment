##########################################################
##
##  File name   : Assigment32Question1.py
##  Descreption : Design automation script which accept directory name
##                and file extension from user. Display all files with that extension.
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.

import sys
import os
import hashlib

def Directoryvaild(DirName):
    return os.path.isdir(DirName)

def calculateCheckSum(path):
    hobj = hashlib.md5()

    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def DisplayCheckSum(Dirname):

    for root,dirs,files in os.walk(Dirname):
        for file in files:

            src_path = os.path.join(root,file)

            print(calculateCheckSum(src_path))

def main():

    if len(sys.argv) != 2:
        print("Invaild agrument entry")
        return

    DirName = sys.argv[1]

    if not Directoryvaild(DirName):
        print("Directory does not exits")
        return

    DisplayCheckSum(DirName)

if __name__ == "__main__":
    main()    