##########################################################
##
##  File name   : Assigment48Question4.py
##  Descreption : Python program to calculate the Euclidean distance between two points before and after applying
##                feature scaling, and explain the difference in results.
##  Author      : Kartik Ganesh Jare
##  Date        : 13/3/26
##
##########################################################

import numpy as np
from sklearn.preprocessing import StandardScaler

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def main():
   data1 =[21,250000]
   data2 =[51,80000]  
   
   d1 = np.array(data1)
   d2 = np.array(data2)

   dist_before = euclidean_distance(d1, d2)

   data = np.array([data1, data2])
   scaler = StandardScaler()
   scaled_data = scaler.fit_transform(data)

   sp1 = scaled_data[0]
   sp2 = scaled_data[1]

   dist_after = euclidean_distance(sp1, sp2)

   print("Distance before scaling:", dist_before)
   print("Distance after scaling:", dist_after)
   
if __name__ == "__main__":
    main()