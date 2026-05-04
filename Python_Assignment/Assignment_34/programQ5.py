#-----------------------------------------------------------------
#
#  File name   : Assigment34Question5.py
#  Descreption : Backup History Tracker
#  Author      : Kartik Ganesh Jare
#  Date        : 11/2/26
#
#-----------------------------------------------------------------

# • Maintain a file:
#       Date
#       Number of files
#       Zip size
# • Display history using:
#       python Script.py --history

import os
import datetime
import sys
import shutil
import time
import zipfile

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    zip_name = folder + "_" +timestamp +".zip"

    file_count = 0 

    # Open the zip file
    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED) 

    for root,dirs,files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)
            file_count += 1

    zobj.close()
    
    return zip_name,file_count

def History(zipfile,filecount):

    history_file = "BackupHistory.txt"

    now = datetime.datetime.now()
    date_time = now.strftime("%d-%m-%Y %H-%M-%S")

    size = os.path.getsize(zipfile)

    entry = f"{date_time} | file: {filecount} | size: {size} bytes\n"

    fobj = open(history_file,"a")

    fobj.write(entry)

def DisplayHistory():

    history_file = "BackupHistory.txt"

    if not os.path.exists(history_file):
        print("No backup history found.")
        return

    print("\n===== Backup History =====\n")

    fobj = open(history_file, "r")
    
    print(fobj.read())    

def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("Backup  : python Script.py SourceFolder")
        print("History : python Script.py --history")
        return
    

    if sys.argv[1] == "--history":
        DisplayHistory()
        return

    src = sys.argv[1]

    zipfile,file_count = make_zip(src)

    History(zipfile,file_count)

    print("Backup created successfully : ",zipfile)
    
if __name__ == "__main__":
    main()