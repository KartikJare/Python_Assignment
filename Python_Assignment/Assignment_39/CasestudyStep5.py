#-----------------------------------------------------------------
#
#  File name   : Assigment39Question5.py
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
    test_size=0.5,
    random_state=42,
)

model = DecisionTreeClassifier(max_depth=5,random_state=42)

model.fit(X_train,Y_train)

print("Model succesfully training")

Y_train_pred = model.predict(X_train)
train_acc = accuracy_score(Y_train,Y_train_pred)

Y_test_pred = model.predict(X_test)
test_acc = accuracy_score(Y_test,Y_test_pred)

print("Train Accutacy: ",train_acc*100)
print("Test  Accutacy: ",test_acc*100)