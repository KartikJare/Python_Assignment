#-----------------------------------------------------------------
#
#  File name   : Assigment34Question1.py
#  Descreption : Logging System
#  Author      : Kartik Ganesh Jare
#  Date        : 11/2/26
#
#-----------------------------------------------------------------

# Create a Logs/ folder
# Store:
#   Backup start time
#   Files copied
#   Zip file name
#   Errors (if any)

import os
import time
import zipfile
import shutil
import sys

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    zip_name = folder + "_" +timestamp +".zip"

    # Open the zip file
    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED) 

    for root,dirs,files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()
    
    return zip_name

def BackupFiles(Source,Destination):
    copied_files =[]
    errors = []

    os.makedirs(Destination,exist_ok=True)

    for root,dirs,files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

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

def MarvellousDataShieldStrat(Source = "Data"):
   
    BackupName = "Backup"

    if not os.path.exists("Log"):
        os.mkdir("Logs")

    start_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    logfile = os.path.join("Logs","Logs_" + timestamp +".txt")
    
    fobj = open(logfile,"w")

    fobj.write(f"Backup start at :  {start_time}\n")

    files,erros = BackupFiles(Source,BackupName)

    zip_file = make_zip(BackupName)

    fobj.write(f"zip file gets create : {zip_file} \n")
    fobj.write(f"Files copied : {len(files)} \n")

    if len(erros) == 0:
        fobj.write("Error : None\n")
    else:
        fobj.write("Erroe : \n")
        for e in erros:
            fobj.write(e + "\n")    


    fobj.write("Backup completed")

    fobj.close()

def main():
    
    if (len(sys.argv) == 2):
        MarvellousDataShieldStrat(sys.argv[1])
    else:
        print("Usage : python Assigment34Question1.py FolderName")

if __name__ == "__main__":
    main()
 