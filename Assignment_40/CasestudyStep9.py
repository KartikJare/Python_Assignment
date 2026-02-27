#-----------------------------------------------------------------
#
#  File name   : Assigment38Question9.py
#  Descreption : Create a plot showing relationship between 
#                AssignmentsCompleted and FinalResult.
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]


plt.boxplot([fail_students["AssignmentsCompleted"],
                pass_students["AssignmentsCompleted"]],
                labels=["Fail", "Pass"])

plt.ylabel("Assignments Completed")
plt.title("Assignments Completed vs Final Result")
plt.show()


# It is showed generally who passed as completed it more assignment that who failed