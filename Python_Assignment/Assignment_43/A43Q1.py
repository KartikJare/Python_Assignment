#=====================================================================================================
# CaseStudy Name     : Student Performance Prediction using Decision Tree
# Input              : student_performance_ml.csv
# Output             : Predicted Final Result with Accuracy Score
# Description        : Builds and evaluates a Decision Tree model to predict student performance.
#                      Includes dataset analysis, model training, prediction, accuracy evaluation,
#                      feature importance extraction, and confusion matrix visualization.
# Author             : Manav Mahadev Jadhav
# Date               : 05/03/2026
#=====================================================================================================
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 50

def CalculateAccuracy(Y_test,Y_pred):

    Result = accuracy_score(Y_test,Y_pred)

    print(Border)
    print("Accuracy of model is  : ",Result*100)
    print(Border)

    return Result

def TestModel(X_test,trained_model):

    Y_pred = trained_model.predict(X_test)

    return Y_pred


def BuildModel(X_train,Y_train,model):


    trained_model = model.fit(X_train,Y_train)

    return trained_model

def SelectModel():

    model = KNeighborsClassifier(n_neighbors=5)

    return model

def SplitTrainingTesting(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)

    return X_train,X_test,Y_train,Y_test

def SplitXY(df):
    X = df[['Whether','Temperature']]
    Y = df['Play']

    print(Border)
    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)
    print(Border)

    return X,Y

def PrepareData(df):

    for col in df.select_dtypes(include='object'):
        df[col]=LabelEncoder().fit_transform(df[col])

    print(Border)
    print("Data after encoding is : ")
    print(Border)
    print(df.head())
    print(Border)

    return df


def CleanData(df):
    
    print(Border)
    print("Shape of data before cleaning  : ",df.shape)
    print(Border)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0', inplace =True)

    print(Border)
    print("Shape of data after cleaning  : ",df.shape)
    print(Border)

    print(Border)
    print("Clean Data is : ")
    print(Border)
    print(df.head())
    print(Border)

    return df

def LoadData():
    df = pd.read_csv("PlayPredictor.csv")
    print(Border)
    print("Few entries from dataset are : ")
    print(df.head())
    print(Border)
    return df


#-----------------------------------------------------------------------------------------------------
# Function    : main
# Description : Driver function that executes the entire workflow
#-----------------------------------------------------------------------------------------------------
def main():
    Dataframe = LoadData()

    df = CleanData(Dataframe)

    df = PrepareData(df)

    X, Y = SplitXY(df)

    X_train,X_test,Y_train,Y_test = SplitTrainingTesting(X,Y)

    model = SelectModel()

    trained_model = BuildModel(X_train,Y_train,model)

    Y_pred = TestModel(X_test,trained_model)

    Result = CalculateAccuracy(Y_test,Y_pred)

#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


# When value of k is 3 , then accuracy is : 83.3333
# When value of k is 5 , then accuracy is : 100.0