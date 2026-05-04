#######################################################################
# File Name : diabetescasestudy.py
# Description : ML model to predict diabetes using accuracy only
# Author : Kartik Ganesh Jare
# Date : 03/04/2026
#######################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv("diabetes.csv")

print("First 5 rows of dataset:")
print(df.head())


print("Dataset Information:")
print(df.info())

print("Missing Values:")
print(df.isnull().sum())

print("Statistical Summary:")
print(df.describe())

plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()

cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in cols:
    df[col] = df[col].replace(0, np.nan)
    df[col].fillna(df[col].mean(), inplace=True)

X = df.drop(columns=['Outcome'])
Y = df['Outcome']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled, Y, test_size=0.2, random_state=42
)

lr = LogisticRegression()
lr.fit(X_train, Y_train)
Y_pred_lr = lr.predict(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
Y_pred_knn = knn.predict(X_test)

dt = DecisionTreeClassifier()
dt.fit(X_train, Y_train)
Y_pred_dt = dt.predict(X_test)

print("Logistic Regression Accuracy :", accuracy_score(Y_test, Y_pred_lr))
print("KNN Accuracy :", accuracy_score(Y_test, Y_pred_knn))
print("Decision Tree Accuracy :", accuracy_score(Y_test, Y_pred_dt))


final_predictions = lr.predict(X_test)

output = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": final_predictions
})

output.to_csv("predictions.csv", index=False)

print("\nPredictions saved successfully in predictions.csv")
