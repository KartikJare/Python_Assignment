##########################################################
##
##  File name   : Assigment23Question1.py
##  Descreption : Python program to implement a class named BookStore
##  Author      : Kartik Ganesh Jare
##  Date        : 25/1/26
##
##########################################################

class BookStore:
    
    NoofBook = 0

    def __init__(self,Name,Author):
        self.BookName = Name
        self.BookAuthor = Author
        BookStore.NoofBook += 1
    
    def Diplay(self):
        print(f"{self.BookName} by {self.BookAuthor}. No of Book {BookStore.NoofBook}")


def main():

    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display() 

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display() 
    
if __name__ == "__main__":
    main()    