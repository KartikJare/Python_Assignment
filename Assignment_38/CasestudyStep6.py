#-----------------------------------------------------------------
#
#  File name   : Assigment38Question6.py
#  Descreption : Plot a histogram of StudyHours
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Explain what the distribution tells you.

import pandas as pd
import matplotlib.pyplot as plt

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

plt.hist(df["StudyHours"])
plt.xlabel("Study hours")
plt.ylabel("Number of Students")
plt.title("histogram of StudyHours")
plt.show()

# 1. If most bars are concentrated in the middle range,
# it means most students study moderate hours.
# 2. If the graph is right side more students with lower hours,
# fewer students study very long hours.
# 3 .If the graph is left side more students with higher hours,
# most students are studying regularly.