#-----------------------------------------------------------------
#
#  File name   : Assigment33Question2.py
#  Descreption : Add Open Files Monitoring Feature
#  Author      : Kartik Ganesh Jare
#  Date        : 11/2/26
#
#-----------------------------------------------------------------

# For each process, display:
# • Number of files opened by the process
# Requirement
# • Count open file descriptors using system/library calls
# • Handle permission errors properly
# • Mention “Access Denied” in log if required

import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
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
    fileName = os.path.join(FolderName,"log_%s.log" %timestamp)
    print("Log file gets created with name : ",fileName)

    fobj = open(fileName,"w")

    fobj.write("----------------System Report-----------------\n")

    # Process LOG
    Data = ProcessScan()
    
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Thread create by the process are : %s\n" %info.get("ThreadNumber"))
        fobj.write("Open file by the process are : %s\n" %info.get("OpenFile"))
        fobj.write(Broder+"\n")
        
    fobj.write(Broder+"\n")
    fobj.write("-------------End of Log Files-------------\n")
    fobj.write(Broder+"\n")


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


def main():
    
    if(len(sys.argv) == 2):
        print("Unable to processd as there is no such option")
               
    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
 
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invaild number of command line argument")

if __name__ == "__main__":
    main()