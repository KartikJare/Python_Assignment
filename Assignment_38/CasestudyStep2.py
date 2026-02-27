#-----------------------------------------------------------------
#
#  File name   : Assigment38Question2.py
#  Descreption : Write a program to
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Display total number of students in the dataset
#   Count how many students Passed (FinalResult = 1)
#   Count how many students Failed (FinalResult = 0)

import pandas as pd

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

print("Total number of students : ",df.shape[0])

pass_studets = df[df["FinalResult"] == 1].shape[0]

fail_studets = df[df["FinalResult"] == 0].shape[0]

print("Number of student passed : ",pass_studets)
print("Number of student failed : ",fail_studets)