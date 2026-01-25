##########################################################
##
##  File name   : Assigment23Question2.py
##  Descreption : Python program to implement a class named BackAccount
##  Author      : Kartik Ganesh Jare
##  Date        : 25/1/26
##
##########################################################

class BackAccount:
    
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.AccountName = Name
        self.AccounBalance = Amount
        

    def Diplay(self):
        print("Account Holder Name : ",self.AccountName)
        print("Account Balance :",self.AccounBalance)

    def Deposit(self):
        dNo = float(input("Enter amount to deposit : "))
        self.AccounBalance = self.AccounBalance + dNo

    def withdraw(self):
        wNo = float(input("Enter amount to withdraw : "))
        if(wNo <= self.AccounBalance):
            self.AccounBalance = self.AccounBalance - wNo
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.AccounBalance * BackAccount.ROI) / 100
        return Interest            

def main():

    obj1 = BackAccount("Kartik",100000)
    obj1.Diplay()
    obj1.Deposit()
    obj1.withdraw()
    print("Interest : ",obj1.CalculateInterest())
    obj1.Diplay()
    
    obj2 = BackAccount("Admit",10000)
    obj2.Diplay()
    obj2.Deposit()
    obj2.withdraw()
    print("Interest : ",obj2.CalculateInterest())
    obj2.Diplay()
    
    
if __name__ == "__main__":
    main()    