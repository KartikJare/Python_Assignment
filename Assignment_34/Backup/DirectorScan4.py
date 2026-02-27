import os
import Demo

def DirectoryScanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName) 
    
    if(Ret==False):
        print("Unable to scan as its not a directory")

    print("Contents of the directory are : ")
    
    for FolderName,SubFolberName,FileName in os.walk(DirectoryName):
        print("Folder name : ",FolderName)

        for subf in SubFolberName:
            print("SubFolber name :",subf)

        for fname in FileName:
            print("File name : ",fname)   

def main():
    DirectoryName = input("Enter th name of directory : ")

    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()    