#-----------------------------------------------------------------
#
#  File name   : Assigment34uestion2.py
#  Descreption : Email Notification
#  Author      : Kartik Ganesh Jare
#  Date        : 11/2/26
#
#-----------------------------------------------------------------

#   Send an email after backup completion
#   Attach:
#       Log file
#       Zip file name

import os
import time
import zipfile
import shutil
import sys
import smtplib
from email.message import EmailMessage
import os

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

def sendEmail(logfile,zipfile,receiver_email):

    Sender_Mail ="pythonkartikauto@gmail.com"
    Password ="guip jomr vpnb muyn"

    msg = EmailMessage()
    msg["subject"] = "Backup completed Successfully"
    msg["From"] = Sender_Mail
    msg["To"] = receiver_email

    body = f"""
    Backup completed successfully.

    Please find attached log file and zip backup.

    Regards,
    Kartik G Jare
    """

    msg.set_content(body)

    fobj = open(logfile,"rb")
    
    filedata = fobj.read()
    filename = os.path.basename(logfile)

    msg.add_attachment(filedata,maintype="application",subtype="octet-stream",filename =filename)

    fobj = open(zipfile,"rb")
    
    filedata = fobj.read()
    filename = os.path.basename(zipfile)

    msg.add_attachment(filedata,maintype="application",subtype="octet-stream",filename =filename)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(Sender_Mail,Password)
    smtp.send_message(msg)

    smtp.quit()

    print("Email sent successfully...")

    fobj.close()


def MarvellousDataShieldStrat(Source = "Data"):
   
    BackupName = "Backup"

    if not os.path.exists("Logs"):
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
    
    sendEmail(logfile,zip_file,"kartikgjare@gmail.com")


def main():
    
    if (len(sys.argv) == 2):
        MarvellousDataShieldStrat(sys.argv[1])
    else:
        print("Usage : python Assigment34Question1.py FolderName")

if __name__ == "__main__":
    main()
 