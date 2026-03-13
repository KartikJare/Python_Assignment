#-----------------------------------------------------------------
#
#  File name   : Assigment40Question4.py
#  Descreption : Create a new DataFrame with details of 5 new students.
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Use the trained model to predict their results.
# Display predictions clearly.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance","PreviousScore","SleepHours"]]
Y = df["FinalResult"]

model = DecisionTreeClassifier()

model.fit(X,Y)

print("model tarining...")

newstudent = pd.DataFrame({
    "StudyHours":[4,5,8,6,7],
    "Attendance":[60,75,90,80,65],
    "PreviousScore":[50,65,85,70,55],
    "SleepHours":[9,3,4,8,7],
})
print("New student data is : ")
print(newstudent)

pred = model.predict(newstudent)

print("predicted result is :",pred)

for i in range(len(pred)):
    if(pred[i] == 1):
        Result = "Pass"
    else:
        Result = "Fails"

    print("Student",i+1,"->",Result)        