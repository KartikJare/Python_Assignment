#-----------------------------------------------------------------
#
#  File name   : Assigment42Question1.py
#  Descreption : Implement Simple Linear Regression manually without 
#                using any ML library.
#  Author      : Kartik Ganesh Jare
#  Date        : 4/3/26
#
#-----------------------------------------------------------------

# Dataset
#   X = [1,2,3,4,5]
#   Y = [3,4,2,4,5]
# Tasks
#   Calculate:
#       1. Mean of X (X̄)
#       2. Mean of Y (Ȳ)
#       3. Slope (m)
#       4. Intercept (c)

import numpy as np

def SimpleLinear():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent variable : X - ",X)
    print("Values of Dependent variable : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_MEAN is : ",mean_x)   
    print("Y_MEAN is : ",mean_y) 

    n = len(X)

    numerator = 0
    denomirator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-mean_x) *(Y[i]-mean_y)) 
        denomirator = denomirator + ((X[i] - mean_x)**2)

    m = numerator / denomirator

    print("Slope of line ie m :",m)   

    C = mean_y - (m * mean_x)

    print("Y intercept pf line ie C : ",C)

    X_new = 6
    Y_pred = (m * X_new) + C

    print("Predicted Y for X = 6 :",round(Y_pred,2))

def main():
    SimpleLinear()


if __name__ == "__main__":
    main()
