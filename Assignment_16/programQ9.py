##########################################################
##
##  File name   : Assigment16Question9.py
##  Descreption : Display frist even number on screen
##  Author      : Kartik Ganesh Jare
##  Date        : 22/1/26
##
##########################################################

def DislpayEven():

    for i in range(1,21):
        if(i % 2 == 0):
            print(i)

def main():

    DislpayEven()

if __name__ == "__main__":
    main()       