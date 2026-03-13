import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

broder = "-"*40

# Step 1 : Load the dataset from CSV file
def LoadData():
    
    print(broder)
    print("Step 1 : Load the dataset from CSV file")
    print(broder) 
    
    df = pd.read_csv("PlayPredictor.csv")
    print(broder)
    print("Some entries from the dataset : ")
    print(df.head())
    print(broder)
    
    return df

# Step 2 : Clean the dataset by removing empty rows
def CleanData(df):
    
    print(broder)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(broder) 

    print(broder)
    print("Shape of data before cleaning  : ",df.shape)
    print(broder)

    if'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0',inplace=True)

    print(broder) 
    print("Shape of data after cleaning  : ",df.shape)
    print(broder) 

    print(broder) 
    print("Clean Data is : ")
    print(broder) 
    print(df.head())
    print(broder)

    return df

def PrepareData(df):
    
    for col in df.select_dtypes(include='object'):
        df[col]=LabelEncoder().fit_transform(df[col])

    print(broder)    
    print("Data after encoding is : ")
    print(broder)  
    print(df.head())
    print(broder)
    
    return df

# Step 3 : Separate indepemdent & Dependent Variable
def SplitXY(df):
    print(broder)
    print("Step 3 : Separate indepemdent & Dependent Variable")
    print(broder) 

    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    return X,Y

# Step 4 : Split the dataset for training and testing
def SplitTrainingTesting(X,Y):
    
    print(broder)
    print("Step 4 : Split the dataset for training and testing")
    print(broder)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print(broder)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    return X_train,X_test,Y_train,Y_test

def SelectModel():
    model = KNeighborsClassifier(n_neighbors=5)

    return model

def BuildModel(X_train,Y_train,model):

    trained_model = model.fit(X_train,Y_train)

    return trained_model

def TestModel(X_test,trained_model):

    Y_pred = trained_model.predict(X_test)

    return Y_pred

def CalculateAccuracy(Y_test,Y_pred):

    Result = accuracy_score(Y_test,Y_pred)

    print(broder)
    print("Accuracy of model is  : ",Result*100)
    print(broder)

    return Result

def main():

    print(broder)
    print("Play predictor using KNN")
    print(broder)

    Dataframe = LoadData() 

    df = CleanData(Dataframe)  

    df = PrepareData(df)
    
    X,Y = SplitXY(df)

    X_train,X_test,Y_train,Y_test = SplitTrainingTesting(X,Y)

    model = SelectModel()

    trained_model = BuildModel(X_train,Y_train,model)

    Y_pred = TestModel(X_test,trained_model)

    Result = CalculateAccuracy(Y_test,Y_pred)

if __name__ == "__main__":
    main()    


# When value of k is 3 , then accuracy is : 83.3333
# When value of k is 5 , then accuracy is : 100.0