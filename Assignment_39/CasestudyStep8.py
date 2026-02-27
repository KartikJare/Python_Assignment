#-----------------------------------------------------------------
#
#  File name   : Assigment38Question8.py
#  Descreption : Draw a boxplot for Attendance.
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

plt.boxplot(df["Attendance"])
plt.ylabel("Attendance")
plt.title("Boxplot of Attendance")
plt.show()