#-----------------------------------------------------------------
#
#  File name   : Assigment33Question4.py
#  Descreption : Add Periodic Email Reporting Feature
#  Author      : Kartik Ganesh Jare
#  Date        : 11/2/26
#
#-----------------------------------------------------------------

# Automatically send system report through email at regular intervals.
# Email must contain:
# • Log file attachment
# • Summary of:
# ◦ Total processes
# ◦ Top CPU usage processes
# ◦ Top Memory usage processes
# ◦ Top Thread count processes
# ◦ Top Open file processes
# Usage
# PlatformSurveillance.py "MarvellousLogs" "receiver@gmail.com" 10

# Where:
# • MarvellousLogs → log folder
# • receiver@gmail.com → receiver mail
# • 10 → interval in minutes

# Expected Output in Log File
# Each process entry should include:
# Process Name
# PID
# CPU %
# Memory (RSS)
# Threads Count
# Open Files Count
# Timestamp

import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

Sender_Mail = "pythonkartikauto@gmail.com"
Password = "guip jomr vpnb muyn"

def CreateLog(FolderName,ReceiverMail):
    Broder = "-"*50
    
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)    
        if(Ret == False):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = os.path.join(FolderName,f"log_{timestamp}.log")
    
    fobj = open(fileName,"w")

    fobj.write("----------------System Report-----------------\n")

    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Broder+"\n")

    # Process LOG
    Data = ProcessScan()
    
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Thread create by the process are : %s\n" %info.get("ThreadNumber"))
        fobj.write("actual RAM used (RSS) : %s MB\n" %(info.get("RSS") / (1024 * 1024)))
        fobj.write("Open file by the process are : %s\n" %info.get("OpenFile"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_precent"))
        fobj.write("Memory  %% : %.2f\n" %info.get("MemoryPrecent"))
        fobj.write(Broder+"\n")
        
    fobj.write(Broder+"\n")
    fobj.write("-------------End of Log Files-------------\n")
    fobj.write(Broder+"\n")

    SendEmail(ReceiverMail,fileName,Data)

def ProcessScan():
    listprocess = []

    # Warm from up CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass    

    time.sleep(0.2)    

    for proc in psutil.process_iter():
        
        try:
            info = proc.as_dict(attrs=["pid","name"])
            #Convert create_time
            try:
                info["create_time"] = time.strftime("%Y-%M-%d %H:%M:%S",time.localtime(info("create_time")))
            except:
                info["create_time"] = "NA"

            info["ThreadNumber"] = proc.num_threads()
            
            meminfo = proc.memory_info()
            info["cpu_precent"] = proc.cpu_percent(None)

            info["RSS"] = meminfo.rss
            info["MemoryPrecent"] = proc.memory_percent()

            try:
                openfile = proc.open_files()
                info["OpenFile"] = len(openfile)
            except psutil.AccessDenied:
                info["OpenFile"] = "Access Denied"
            except:
                info["OpenFile"] = "NA"

        
            listprocess.append(info)         
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess    

def SendEmail(receiver,filename,Data):
    msg = EmailMessage()
    msg["From"] = Sender_Mail
    msg["To"] = receiver
    msg["Subject"] = "System Report"

    body = f"""
    SYSTEM REPORT SUMMARY

    Please check attached log file for full details.

    Regards,
    Kartik G Jare
    """
    msg.set_content(body)

    fobj = open(filename,"rb")
    
    filedata = fobj.read()
        
    msg.add_attachment(filedata,
                       maintype="application",
                       subtype="octet-stream",
                       filename=os.path.basename(filename)
                       )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(Sender_Mail,Password)
    smtp.send_message(msg)

    smtp.quit()

    print("Email sent successfully...")

    fobj.close()

def main():
       
    # PlatformSurveillance.py "MarvellousLogs" "receiver@gmail.com" 10
    if(len(sys.argv) == 4):

        folderName = sys.argv[1]
        recivermailid =  sys.argv[2]
        interval = int(sys.argv[3])

        schedule.every(interval).minutes.do(CreateLog,folderName,recivermailid)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invaild number of command line argument")

if __name__ == "__main__":
    main()