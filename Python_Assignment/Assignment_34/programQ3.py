#-----------------------------------------------------------------
#
#  File name   : Assigment34Question3.py
#  Descreption : Restore Feature
#  Author      : Kartik Ganesh Jare
#  Date        : 11/2/26
#
#-----------------------------------------------------------------

# Add a command:
#   python Script.py --restore ZipFileName Destination
#   Extract backup to given directory

import os
import zipfile
import sys

def Restorezip(zip_file,Destination):

    if not os.path.exists(zip_file):
        print("Error : There is no such file.")
        return
    
    if not os.path.exists(Destination):
        os.makedirs(Destination)
    
    try:
        zobj = zipfile.ZipFile(zip_file,"r")

        zobj.extractall(Destination)

        print("Backup restored successfully")
    except Exception as e:
        print("Error while restoring backup: ",e)

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return

    if sys.argv[1] == "--restore":

        print("Usage : python Script.py ZipFileName Destination")
        return

    elif len(sys.argv) == 3:

        zip_file = sys.argv[1]
        destination = sys.argv[2]

        Restorezip(zip_file, destination)

    else:
        print("Invalid option")  

    
if __name__ == "__main__":
    main()