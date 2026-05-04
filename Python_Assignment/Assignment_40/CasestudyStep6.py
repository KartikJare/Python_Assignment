#-----------------------------------------------------------------
#
#  File name   : Assigment40Question6.py
#  Descreption : Identify students where 
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# y_test != y_pred
# • Display those rows.
# • How many students were misclassified?
# • What common pattern do you observe?

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

model = DecisionTreeClassifier()

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

misclassified = X_test[Y_test != Y_pred]

print("Misclassified student are : ")
print(misclassified)

if misclassified.empty:
    print("No students were misclassified.")
else:
    print(misclassified)

iCount = len(misclassified)

print("Total misclassified student : ",iCount)