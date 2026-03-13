#-----------------------------------------------------------------
#
#  File name   : Assigment40Question1.py
#  Descreption : After training the Decision Tree model,use
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# model.feature_importances_
# • Display importance score of each feature.
# • Which feature contributes the most in predicting FinalResult?
# • Which feature contributes the least?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

X = df[["StudyHours","Attendance","PreviousScore"]]
Y = df["FinalResult"]

model = DecisionTreeClassifier()
model.fit(X,Y)

imp = model.feature_importances_

feature_importance_series = pd.Series(imp, index=X.columns).sort_values(ascending=False)

print("Importance Feature are: ")
print(feature_importance_series)

most_important = feature_importance_series.idxmax()
least_important = feature_importance_series.idxmin()

print("Feature most contributing in predict finalresult : ",most_important)
print("Feature least contributing in predict finalresult : ",least_important)