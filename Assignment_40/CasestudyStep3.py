#-----------------------------------------------------------------
#
#  File name   : Assigment38Question3.py
#  Descreption : Using pandas functions, calculate and display
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Average StudyHours
#   Average Attendance
#   Maximum PreviousScore
#   Minimum SleepHours

import pandas as pd

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

Average_studyhours = df["StudyHours"].mean()
Average_Attendance = df["Attendance"].mean()
max_PreviousScore = df["PreviousScore"].max()
Min_SleepHours = df["SleepHours"].min()


print("Average study hours is : ",Average_studyhours)
print("Average Attendance is : ",Average_Attendance)
print("Maximum previous score is : ",max_PreviousScore)
print("Minimum Sleep hours is : ",Min_SleepHours)