#-----------------------------------------------------------------
#
#  File name   : Assigment38Question4.py
#  Descreption : Use value_counts() to analyze the distribution of FinalResult.
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer

import pandas as pd

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

result = df["FinalResult"].value_counts()

result_percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("Final Result count : ",result)

print("Final result in percentage : ",result_percentage)

pass_percent = result_percentage.get(1,0)
fail_percent = result_percentage.get(0,0)

# Data is not balanced is a imbalanced dataset there is a large different between classses 
