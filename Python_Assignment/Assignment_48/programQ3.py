##########################################################
##
##  File name   : Assigment48Question3.py
##  Descreption : Python program using StandardScaler to perform feature scaling on the following dataset
##                Print the scaled dataset
##  Author      : Kartik Ganesh Jare
##  Date        : 13/3/26
##
##########################################################

# [[25,20000],
# [30,40000],
# [35,80000]]

import numpy as np
from sklearn.preprocessing import StandardScaler

data = [[25,20000],
        [30,40000],
        [35,80000]]

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("Scaled Dataset:")
print(scaled_data)

