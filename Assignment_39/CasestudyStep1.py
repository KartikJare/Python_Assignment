#-----------------------------------------------------------------
#
#  File name   : Assigment39Question1.py
#  Descreption : Import DecisionTreeClassifier from sklearn
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Create a model object and train it using fit().

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42,
)

model = DecisionTreeClassifier(max_depth=5,random_state=42)

model.fit(X_train,Y_train)

print("Model succesfully training")

