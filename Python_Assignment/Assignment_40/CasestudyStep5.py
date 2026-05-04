#-----------------------------------------------------------------
#
#  File name   : Assigment40Question5.py
#  Descreption : Without using accuracy_score, manually calculate accuracy
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   Verify whether it matches sklearn accuracy.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance","PreviousScore","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
)

model = DecisionTreeClassifier(max_depth=5,random_state=42)

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

sum = 0

for i in range(len(Y_test)):
    if(Y_pred[i] == Y_test.iloc[i]):
        sum += 1

accuracy_scoreX = sum / len(Y_test)

print("Accuarcy scoreX is : ",accuracy_scoreX*100)


accuracy = accuracy_score(Y_test,Y_pred)

print("Sklearn accuray is : ",accuracy*100)