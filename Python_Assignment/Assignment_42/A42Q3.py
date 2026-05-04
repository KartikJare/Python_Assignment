import numpy as np
import matplotlib.pyplot as plt

def SimpleLinearRegression(X,Y,value):
    print("X = ", X)
    print("Y = ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_bar  = ",mean_x)
    print("Y_bar  = ",mean_y)

    n = len(X)

# Y = mX + C

# m = (summ (X-X_bar) * (Y-Y_bar)) /  (Summ (X -X_bar)**2)   
    numerator = 0 
    denominator = 0
 
    for i in range(n):
        numerator += ((X[i] - mean_x)* (Y[i] - mean_y))
        denominator += ((X[i]- mean_x)**2)

    m = numerator /denominator

    print("Slope of line ie m is : ",m)

    C = mean_y - (m * mean_x)

    print("Y-Intercept of line i.e C : ",C)
    
    Result = m * value + C
    print(f"Predicted Y for {value} is : {Result}")

    x = np.linspace(1,6,n)
    y = C + m * x

    plt.plot(x,y,color = 'g', label ="Regression Line")
    plt.scatter(X,Y,color = 'r' , label ="Scatter plot")

    plt.xlabel("X : Independent variable")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()
    

def main():
    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

    print("Enter the value of X that needs to be predicted : ")
    value = int(input())

    SimpleLinearRegression(X,Y,value)

if __name__ == "__main__":
    main()