#-----------------------------------------------------------------
#
#  File name   : Assigment38Question1.py
#  Descreption : Python program to load the file student_performance_ml.csv using pandas.
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Display:
#       First 5 records
#       Last 5 records
#       Total number of rows and columns
#       List of column names
#       Data types of each column

import pandas as pd

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

print("Frist 5 records :")
print(df.head())

print("Last 5 records :")
print(df.tail())

print("Total number of rows and colums : ",df.shape)

print("List of column names : ")
print(df.columns.to_list())  # new

print("Data types of each column : ")
print(df.dtypes)
