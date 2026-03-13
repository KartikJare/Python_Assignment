#-----------------------------------------------------------------
#
#  File name   : Assigment42Question2.py
#  Descreption : Using the same dataset from above question, calculate 
#                model performance.
#  Author      : Kartik Ganesh Jare
#  Date        : 4/3/26
#
#-----------------------------------------------------------------

# Tasks
# 1. Predict all Y values using regression equation.
# 2. Calculate:
# • Mean Squared Error (MSE)
# • R2 Score
# Show all intermediate calculations.

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

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

    # y_pred = []

    # print("Actual predicted of Y is : ")
    
    # for i in range(n):
    #     pred = (m * X[i]) + C
    #     y_pred .append(pred)

    mse = mean_squared_error(Y,Y_pred)
    r2 = r2_score(Y,Y_pred)

    print("Mean sqaured error is : ",mse)
    print("R square value : ",r2)
   
def main():
    SimpleLinear()


if __name__ == "__main__":
    main()
