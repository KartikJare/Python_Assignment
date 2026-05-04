#-----------------------------------------------------------------
#
#  File name   : Assigment41Question1.py
#  Descreption : Write a Python program that classifies a new data point 
#                using the K-Nearest Neighbors algorithm.
#  Author      : Kartik Ganesh Jare
#  Date        : 4/3/26
#
#-----------------------------------------------------------------

# Dataset
# Point  X   Y   Label
#   A    1   2    Red
#   B    2   3    Red
#   C    3   1    Blue
#   D    6   5    Blue

import numpy as np
import math

def Euclideandistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans


def KNeighborsClassifierX(x,y):

    data = [{'point':'A','X': 1,'Y' : 2,'label':'Red'},
            {'point':'B','X': 2,'Y' : 3,'label':'Red'},
            {'point':'C','X': 3,'Y' : 1,'label':'Blue'},
            {'point':'D','X': 6,'Y' : 5,'label':'Blue'},
            ]
    
    for i in data:
        print(i)

    new_point = {'X':x,'Y':y}

    for d in data:
        d['distance'] = Euclideandistance(d,new_point)

    print("Calculated distance are : ")

    for d in data:
        print(d)  

    sorted_data = sorted(data,key=lambda item : item['distance'])

    print("Sorted data is: ")

    for d in sorted_data:
        print(d)

    k = 3     

    nearest = sorted_data[:k]

    print("Nearest 3 element are : ") 

    for d in nearest:
        print(d)       
    
    votes = {}

    for neighbour in nearest:
        label = neighbour['label'] 
        votes[label] = votes.get(label,0) + 1

    print("Voting result is : ")

    for d in votes:
        print("Name : ",d,"Number of votes",votes[d])

    predicted_class = max(votes,key=votes.get)

    print(f"Predicted class of{x,y} is : ",predicted_class)
        
def main():

    x = int(input("Enter X coordinate :"))
    y = int(input("Enter Y coordinate :"))

    KNeighborsClassifierX(x,y)

if __name__ == "__main__":
    main()            