#-----------------------------------------------------------------
#
#  File name   : Assigment41Question3.py
#  Descreption : Use KNN to predict whether a student passes or fails \
#                based on study hours and attendance
#  Author      : Kartik Ganesh Jare
#  Date        : 4/3/26
#
#-----------------------------------------------------------------

# The value of K plays an important role in the KNN algorithm

# Dataset
# StudyHours     Attendance     Result  
#   2                 60           Fail
#   5                 80           Pass
#   6                 85           Pass
#   1                 50           Fail
# 

import numpy as np
import math

def Euclideandistance(P1,P2):
    Ans = math.sqrt((P1['StudyHours'] - P2['StudyHours'])**2 + (P1['Attendance'] - P2['Attendance'])**2)
    return Ans


def KNeighborsClassifierX(x,y):

    data = [{'StudyHours': 2, 'Attendance' : 60,'Result':'Fail'},
            {'StudyHours': 5, 'Attendance' : 80,'Result':'Pass'},
            {'StudyHours': 6, 'Attendance' : 85,'Result':'Pass'},
            {'StudyHours': 1, 'Attendance' : 50,'Result':'Fail'},
            ]
    
    for i in data:
        print(i)

    new_point = {'StudyHours':x,'Attendance':y}

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
        Result = neighbour['Result'] 
        votes[Result] = votes.get(Result,0) + 1

    print("Voting result is : ")

    for d in votes:
        print("Name : ",d,"Number of votes",votes[d])

    predicted_class = max(votes,key=votes.get)

    print(f"Predicted class of{x,y} is : ",predicted_class)
        
def main():

    x = int(input("Enter Study Hours :"))
    y = int(input("Enter Attendance :"))

    KNeighborsClassifierX(x,y)

if __name__ == "__main__":
    main()            


# So prediction may change when K increases 
# because more neighbors influence the voting.