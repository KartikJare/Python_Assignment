#-----------------------------------------------------------------
#
#  File name   : Assigment40Question8.py
#  Descreption : Decision Tree Visualization
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Use:
# from sklearn.tree import plot_tree
# Visualize the trained decision tree.
# • Which feature appears at the root node?
# • Why do you think that feature was selected first?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance","PreviousScore","SleepHours"]]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42   #100
)

model = DecisionTreeClassifier(max_depth=5,random_state=42)

model.fit(X_train,Y_train)

plt.figure(figsize=(12,8))

plot_tree(model,feature_names=X.columns,class_names=["Fail","Pass"],filled=True)

plt.title("Decision Tree Visualization")

plt.show()