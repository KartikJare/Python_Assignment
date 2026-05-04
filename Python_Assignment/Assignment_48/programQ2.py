##########################################################
##
##  File name   : Assigment48Question2.py
##  Descreption : Python program that calculates the variance and standard deviation of the dataset
##  Author      : Kartik Ganesh Jare
##  Date        : 13/3/26
##
##########################################################

# [6, 7, 8, 9, 10, 11, 12]

import numpy as np

data = [6, 7, 8, 9, 10, 11, 12]

variance_value = np.var(data)

standard_deviation_value = np.std(data)

print("variance of data is : ",variance_value)
print("standard deviation of data is : ",standard_deviation_value)