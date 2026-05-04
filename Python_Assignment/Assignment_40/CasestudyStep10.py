#-----------------------------------------------------------------
#
#  File name   : Assigment40Question10.py
#  Descreption : Train model with
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#   max_depth = None
# Calculate:
#   Training accuracy
#   Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance","AssignmentsCompleted","PreviousScore","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
)

model = DecisionTreeClassifier(max_depth=None,random_state=42)

model.fit(X_train,Y_train)

Y_Trainpred = model.predict(X_train)

Y_Testpred = model.predict(X_test)

trainaccuracy= accuracy_score(Y_train,Y_Trainpred)
testaccuracy= accuracy_score(Y_test,Y_Testpred)

print("Train Accuracy of model is : ",trainaccuracy*100)
print("Test Accuracy of model is : ",testaccuracy*100)


# 100 % only of both

