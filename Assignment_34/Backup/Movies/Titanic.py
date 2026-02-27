import os

def main():
    DirectoryName = input("Enter th name of directory : ")

    print("Contents of the directory are : ")

    for FolderName,SubFolberName,FileName in os.walk(DirectoryName):
        print("Folder name : ",FolderName)

        for subf in SubFolberName:
            print("SubFolber name :",subf)

        for fname in FileName:
            print("File name : ",fname)    

if __name__ == "__main__":
    main()    