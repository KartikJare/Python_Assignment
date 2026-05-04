#-----------------------------------------------------------------
#
#  File name   : Assigment34Question4.py
#  Descreption : Exclude Files / Folders
#  Author      : Kartik Ganesh Jare
#  Date        : 11/2/26
#
#-----------------------------------------------------------------

# • Ignore:
#       .tmp, .log, .exe
#       or user-defined extensions


import os
import sys
import shutil
import zipfile

def BackupFiles(Source,Destination):
    copied_files =[]
    errors = []

    excluded_ext = [".tmp",".log",".exe"]

    os.makedirs(Destination,exist_ok=True)

    for root,dirs,files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            _,ext = os.path.splitext(file)

            if ext.lower() in excluded_ext:
                print("Skipped:",file)
                continue

            relative = os.path.relpath(src_path,Source)
            dest_path  =os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            try:
                if((not os.path.exists(dest_path))):
                    shutil.copy2(src_path,dest_path)
                    copied_files.append(relative)
            except Exception as error:
                errors.append(str(error))    

    return copied_files,errors


def main():

    if (len(sys.argv) != 3):
        print("Usage : python Assigment34Question4.py SourceFolder Destion")
        return

    Src = sys.argv[1]
    Destination = sys.argv[2]

    BackupFiles(Src,Destination)
    
if __name__ == "__main__":
    main()