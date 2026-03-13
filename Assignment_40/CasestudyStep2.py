#-----------------------------------------------------------------
#
#  File name   : Assigment40Question2.py
#  Descreption : Remove the column SleepHours from the dataset
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Train the model again.
# Compare new accuracy with previous accuracy.
# Does removing this feature affect performance?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

# With Sleep Hours

X1 = df[["StudyHours","Attendance","PreviousScore","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X1,
    Y,
    test_size=0.2,
    random_state=42,
)

model1 = DecisionTreeClassifier(max_depth=5,random_state=42)

model1.fit(X_train,Y_train)

Y_pred1 = model1.predict(X_test)

accuracy1= accuracy_score(Y_test,Y_pred1)

print("Accuracy of model is with sleephours : ",accuracy1*100)

# without sleephours

X2 = df[["StudyHours","Attendance","PreviousScore"]]

X_train2,X_test2,Y_train2,Y_test2 = train_test_split(
    X2,
    Y,
    test_size=0.2,
    random_state=42,
)

model2 = DecisionTreeClassifier(max_depth=3,random_state=42)

model2.fit(X_train2,Y_train2)

Y_pred2 = model2.predict(X_test2)

accuracy2= accuracy_score(Y_test2,Y_pred2)

print("Accuracy of model is without sleephours : ",accuracy2*100)

if accuracy1 > accuracy2:
    print("Removing SleepHours decreased model performance.")
elif accuracy1 < accuracy2:
    print("Removing SleepHours improved model performance.")
else:
    print("Removing SleepHours did not affect performance.")