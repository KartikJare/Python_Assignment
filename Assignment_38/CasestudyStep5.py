#-----------------------------------------------------------------
#
#  File name   : Assigment38Question5.py
#  Descreption : Based on the dataset values, analyze whether
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Higher StudyHours increase the chance of passing.
#   Higher Attendance improves FinalResult.
#   Write your observations in 4–5 lines.

import pandas as pd

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

pass_data = df[df["FinalResult"] == 1] 
fail_data = df[df["FinalResult"] == 0]

Average_pass = pass_data["StudyHours"].mean()
Average_fail = fail_data["StudyHours"].mean()

Attendance_pass = pass_data["Attendance"].mean()
Attendance_fail = fail_data["Attendance"].mean()

print("Average studyHours of pass : ",Average_pass)
print("Average studyHours of fail : ",Average_fail)

print("Average Attendance Pass:",Attendance_pass)
print("Average Attendance Fail:",Attendance_fail)

# 1.Those who pass are having higher studyhour compared to who fail
# 2.Similarly,student  with higher Attendance percentage tend to have better result
# 3.Regular attendance appears to improve understanding and performance in exams.
# 4.Both studyHours and attendance show a positive correlation with passing results.