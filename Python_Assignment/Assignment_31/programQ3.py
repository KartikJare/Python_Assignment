#----------------------------------------------------------
#
#   File name   : Assigment31Question3.py
#   Descreption : Design automation script which accept two directory names.Copy all files from first 
#                 directory into second directory. Second directory should be created at run time.
#   Date        : 2/2/26
#
#----------------------------------------------------------

# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp.

import sys
import os
import shutil

def Directoryvaild(DirName):
    return os.path.isdir(DirName)

def DirectoryCopy(Source,Destination):

    copied_files = []

    os.makedirs(Destination,exist_ok= True)

    for root,dirs,files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path  =os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            try:           
                shutil.copy2(src_path,dest_path)
                copied_files.append(relative)
            except:
                print("ERR")    

    return copied_files            

def main():

    if len(sys.argv) != 3:
        print("Invaild agrument entry")
        return

    Source = sys.argv[1]
    Destination = sys.argv[2]

    if not Directoryvaild(Source):
        print("Directory does not exits")
        return

    Ret = DirectoryCopy(Source,Destination)

    if len(Ret) == 0:
        print("NO file found to copy")
    else:
        print("File copied successfully",Ret)
        print("End of copy process completed successfully")

if __name__ == "__main__":
    main()    