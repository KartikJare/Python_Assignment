#-----------------------------------------------------------------
#
#  File name   : Assigment39Question7.py
#  Descreption : Use the trained model to predict result for a student with
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

#  StudyHours = 6
#  Attendance = 85
#  PreviousScore = 66
#  AssignmentsCompleted = 7
#  SleepHours = 7
# Will the student Pass or Fail?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
)

model = DecisionTreeClassifier(max_depth=3,random_state=42)   #3 = 100

model.fit(X_train,Y_train)

print("Model succesfully training")

new_data = [[6,85,66,7,7]]

# new_data = pd.DataFrame({
#     "StudyHours": [6],
#     "Attendance": [85],
#     "PreviousScore": [66],
#     "AssignmentsCompleted": [7],
#     "SleepHours": [7]
# })

pre = model.predict(new_data)

if pre[0] == 1:
    print("Prec : pass")
else:
    print("prec : fail")    