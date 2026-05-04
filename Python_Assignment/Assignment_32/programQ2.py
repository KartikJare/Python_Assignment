#-----------------------------------------------------------------
#
#   File name   : Assigment32Question2.py
#   Descreption : Design automation script which accept directory name and write names of duplicate files from
#                 that directory into log file named as Log.txt. Log.txt file should be created into current directory.
#   Author      : Kartik Ganesh Jare
#   Date        : 2/2/26
#
#-----------------------------------------------------------------

# Usage : DirectoryDusplicate.py “Demo”
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

def FindDuplicate(Dirname):
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
                Duplicate[Checksum].append(file)
            else:
                Duplicate[Checksum] = [file]

    return Duplicate   

def LogFile(Dulpicate):
    
    LogFileName = "Log.txt"

    fobj = open(LogFileName,"w")

    fobj.write("Dulpicate File Report\n") 

    for CheckSum,files in Dulpicate.items():

        if len(files) > 1:

            fobj.write("Duplicate Files:\n")

            for file in files:
                fobj.write(file + "\n")

            fobj.write("\n")

    print("Log.txt created successfully.")        

def main():

    if len(sys.argv) != 2:
        print("Invaild agrument entry")
        return

    DirName = sys.argv[1]

    if not Directoryvaild(DirName):
        print("Directory does not exits")
        return

    duplicates = FindDuplicate(DirName)
    LogFile(duplicates)

if __name__ == "__main__":
    main()    