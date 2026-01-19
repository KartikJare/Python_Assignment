##########################################################
##
##  File name   : Assigment15Question7.py
##  Descreption : lambda using filter() which accepts a list of strings
##                and returns a list of strings having length greater than 5.
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

def main():
    Data = ['Pyhton','C','C++','Java','Kartik','Pune']

    RData = list(filter((lambda char : len(char) > 5),Data))
    
    print("Strings having length greater than 5 : ",RData)

if __name__ == "__main__":
    main()       