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

import os

def Filevaild(DirName):
    return os.path.isdir(DirName)

def serachFile(DirName,Extension):

    File = []

    for FolberName,subFolder,FileName in os.walk(DirName):
        print("Folder name : ",FolberName)

        for fname in FileName:
            if fname.endswith(Extension):
                File.append(fname)

    return File            


