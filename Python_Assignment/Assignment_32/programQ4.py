#-----------------------------------------------------------------
#
#   File name   : Assigment32Question4.py
#   Descreption : Design automation script which accept directory name and delete all duplicate files
#                 from that directory. Write names of duplicate files from that directory into log file 
#                 named as Log.txt. Log.txt file should be created into current directory. 
#                 Display execution time required for the script.
#   Author      : Kartik Ganesh Jare
#   Date        : 2/2/26
#
#-----------------------------------------------------------------

# Usage : DirectoryDusplicateRemoval.py “Demo”
# Demo is name of directory.

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

def FindDeleteDuplicate(Dirname):

    LogFilename = "Log.txt"
    fobj = open(LogFilename,"w")

    Ret = False

    Ret = os.path.exists(Dirname)
    if(Ret == False):
        print("Ther is no such directory")
        return
    
    Ret = os.path.isdir(Dirname)
    if(Ret == False):
        print("It is not a Diretocry")
        return

    Duplicate = {}

    for FolberName,SubFolberName,FileName in os.walk(Dirname):
        for file in FileName:
            file = os.path.join(FolberName,file)
            Checksum = calculateCheckSum(file)

            if Checksum in Duplicate:
                os.remove(file)
                fobj.write(file + "\n")
            else:
                Duplicate[Checksum] = file

    fobj.close()
    print("Dulicate file deleted successfully")
    print("Log file created as Log.txt")
     
def main():

    if len(sys.argv) != 2:
        print("Invaild agrument entry")
        return

    DirName = sys.argv[1]
    FindDeleteDuplicate(DirName)

if __name__ == "__main__":
    main()    