##########################################################
##
##  File name   : Assigment31Question2.py
##  Descreption : Design automation script which accept directory name and two file extensions from user.
##                Rename all files with first file extension with the second file extenntion.
##  Author      : Kartik Ganesh Jare
##  Date        : 2/2/26
##
##########################################################

# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename
# with .doc.
# After execution this script each .txt file gets renamed as .doc.

import os

def Filevaild(DirName):
    return os.path.isdir(DirName)

def RenameFile(DirName,oldext,newext):

    renameFile = []

    for FolberName,subFolder,FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(oldext):
                oldpath = os.path.join(FolberName,fname)
                newname = fname.replace(oldext, newext)
                newpath = os.path.join(FolberName,newname)

            try:
                os.rename(oldpath,newpath)
                renameFile.append(newpath)    
            finally:
                print("End of Application")    

    return renameFile            


