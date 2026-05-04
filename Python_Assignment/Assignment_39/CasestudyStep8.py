#-----------------------------------------------------------------
#
#  File name   : Assigment39Question8.py
#  Descreption : Write a single structured Python program that performs
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# 1. Dataset loading
# 2. Data analysis
# 3. Visualization
# 4. Train-test split
# 5. Model training
# 6. Prediction
# 7. Accuracy calculation
# 8. Confusion matrix generation
# 9. Final conclusion

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

########################################################################
#  Step 1 : Load the dataset
########################################################################

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

########################################################################
#  Step 2 : Data analysis
########################################################################

print("Initial entries from dataset:")
print(df.head())

print("Dataset info:")
print(df.info())

print("Missing values (per Column)")
print(df.isnull().sum())    

print("Stastical Report of dataset")
print(df.describe())

########################################################################
#  Step 3 : Visualization
########################################################################

plt.figure()
sns.boxplot(x="FinalResult", y="StudyHours", data=df)
plt.title("Study Hours vs Final Result")
plt.show()

########################################################################
#  Step 4 : Train-test split
########################################################################

feature_cols = [
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

X = df[feature_cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
)

########################################################################
#  Step 5 : Model training
########################################################################

model = DecisionTreeClassifier(max_depth=3,random_state=42)

model.fit(X_train,Y_train)

print("Model trained successfully..")

########################################################################
#  Step 6 : Prediction
########################################################################

Y_pred = model.predict(X_test)

print("Model evalution (testing) complete")

print(Y_pred.shape)

print("Expected answer : ")
print(Y_test)

print("Predicted answer :")
print(Y_pred)

########################################################################
#  Step 7 : Accuracy calculation
########################################################################

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of model is : ",accuracy*100)

########################################################################
#  Step 8 : Confusion matrix generation
########################################################################

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion matix : ")
print(cm)

print("Classification Report")
print(classification_report(Y_test,Y_pred))

Data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)

Data.plot()
plt.title("Confusion matrix of Iris dataset")
plt.show()

########################################################################
#  Step 9 : Final conclusion
########################################################################

if(accuracy > 0.85):
    print("Model performs well and generalizes properly")
else:
    print("Model performance is not optimal. Tune hyperparameters")






