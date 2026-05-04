##########################################################
##
##  File name   : Assigment48Question8.py
##  Descreption : Python program that calculates TP, TN, FP, FN for the following arrays
##  Author      : Kartik Ganesh Jare
##  Date        : 13/3/26
##
##########################################################

# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]

from sklearn.metrics import confusion_matrix

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    cm = confusion_matrix(actual,predicted)

    TN = cm[0][0]
    TN = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    TP = cm[1][1]

    print("True Positive (TP) :", TP)
    print("True Negative (TN) :", TN)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)

if __name__ == "__main__":
    main()    