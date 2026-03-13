#-----------------------------------------------------------------
#
#  File name   : Assigment39Question6.py
#  Descreption : Calculate
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Training accuracy
# Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score)


Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
)

# model = DecisionTreeClassifier(random_state=42)    None = 100
# model = DecisionTreeClassifier(max_depth=1,random_state=42)    #1 = 100
model = DecisionTreeClassifier(max_depth=3,random_state=42)   #3 = 100

model.fit(X_train,Y_train)

print("Model succesfully training")

Y_pred = model.predict(X_test)

print(Y_pred.shape)

print("Expected answer : ")
print(Y_test)

print("Predicted answer :")
print(Y_pred)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of model is : ",accuracy*100)