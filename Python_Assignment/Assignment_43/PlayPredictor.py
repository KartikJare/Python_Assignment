import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

broder = "-"*40

def Playpred(DataPath):
    broder = "-"*40

    # Step 1 : Load the dataset from CSV file

    print(broder)
    print("Step 1 : Load the dataset from CSV file")
    print(broder) 
    
    df = pd.read_csv(DataPath)
    print(broder)
    print("Some entries from the dataset : ")
    print(df.head())
    print(broder)

    for col in df.select_dtypes(include='object'):
        df[col]=LabelEncoder().fit_transform(df[col])

    print(broder)    
    print("Data after encoding is : ")
    print(broder)  
    print(df.head())
    print(broder)

    # Step 2 : Clean the dataset by removing empty rows

    print(broder)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(broder) 

    print(broder)
    print("Shape of data before cleaning  : ",df.shape)
    print(broder)

    if'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0',inplace=True)

    # df.dropna(inplace=True)
    print(broder) 
    print("Shape of data after cleaning  : ",df.shape)
    print(broder) 

    print(broder) 
    print("Clean Data is : ")
    print(broder) 
    print(df.head())
    print(broder) 
    print("Total record : ",df.shape[0])
    print("Total Cloums : ",df.shape[1])

    # Step 3 : Separate indepemdent & Dependent Variable

    print(broder)
    print("Step 3 : Separate indepemdent & Dependent Variable")
    print(broder) 

    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)


    # Step 4 : Split the dataset for training and testing

    print(broder)
    print("Step 4 : Split the dataset for training and testing")
    print(broder)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(broder)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    # Step 6 : Explore the multiple values of k 

    print(broder)
    print("Step 6 : Explore the multiple values of k")
    print(broder)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train,Y_train)
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(broder)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)
    print(broder)

    # Step 8 : Find best value of K

    print(broder)
    print("Step 8 : Find best value of K")
    print(broder)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))] 

    print("Best Values of K is : ",best_k)

    # Step 9 : Bulid final model using best value of k

    print(broder)
    print("Step 9 : Bulid final model using best value of k")
    print(broder)

    finally_model = KNeighborsClassifier(n_neighbors=best_k)

    finally_model.fit(X_train,Y_train)
    Y_pred = finally_model.predict(X_test)

    # Step 10 : Calculate final accuracy

    print(broder)
    print("Step 10 : Calculate final accuracy")
    print(broder)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is : ",accuracy*100)

def main():

    print(broder)
    print("Play predictor using KNN")
    print(broder)

    Playpred("PlayPredictor.csv")

if __name__ == "__main__":
    main()    
