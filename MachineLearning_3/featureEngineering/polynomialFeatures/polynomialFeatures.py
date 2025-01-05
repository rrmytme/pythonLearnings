import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("Age_Height.csv")
print(f"top 5 records are: \n{data.head()}")
print(f"last 5 records are: \n{data.tail()}")
print(f"rows and column sizes: \n{data.shape}")

# set X and y 
x = data.iloc[:,0:1].values
y = data.iloc[:,1].values
#print(x, y)

# Splitting into train and test dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

# Polynomial Regression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 

poly = PolynomialFeatures(degree = 2) 
X_poly = poly.fit_transform(X_train) 
print(f"after Polynomial Features: \n{X_poly}")

# Fitting the polynomial regression model
polyreg = LinearRegression() 
polyreg.fit(X_poly, y_train) 

LinearRegression()

# Evaluating the model
y_pred_pr = polyreg.predict(poly.fit_transform(X_test))
from sklearn.metrics import r2_score
print('R2 score for Polynomial Regression: \n',r2_score(y_test,y_pred_pr))

# Predicting the result
sample = data.sample(1)
sampleAge = sample.values[0,0]
sampleHeight = sample.values[0,1]
print(f"Actual Height for {sampleAge} is: \n{sampleHeight}") 
print(f"Predicted Height for {sampleAge} is: \n{polyreg.predict(poly.fit_transform([[sampleAge]]))}") 