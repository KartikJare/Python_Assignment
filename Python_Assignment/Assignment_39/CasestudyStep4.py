#-----------------------------------------------------------------
#
#  File name   : Assigment39Question4.py
#  Descreption : Generate confusion matrix using sklearn.
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Display it using ConfusionMatrixDisplay.
#  Explain clearly:
#       True Positive
#       True Negative
#       False Positive
#       False Negative

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix,ConfusionMatrixDisplay)
import matplotlib.pyplot as plt

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

Y_pred = model.predict(X_test)

print(Y_pred.shape)

print("Expected answer : ")
print(Y_test)

print("Predicted answer :")
print(Y_pred)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of model is : ",accuracy*100)

cm = confusion_matrix(Y_test,Y_pred)

Data = ConfusionMatrixDisplay(confusion_matrix=cm)
Data.plot()

plt.title("Student Performace")
plt.show()


