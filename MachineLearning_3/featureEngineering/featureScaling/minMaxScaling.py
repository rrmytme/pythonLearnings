'''
Feature Scaling is a method of feature engineering that involves transforming features. 
The features are transformed into floats within a boundary of values, usually between 0 and 1. 
The features, being within the same boundary have none dominating the other.

Min-Max Scaling (Normalization): Min-max is a feature scaling technique that normalizes features in a 
dataset between a minimum and maximum value.

Let's consider a dataset that contains information about students, including their age, test scores, and 
grades. We will demonstrate two feature scaling techniques: Min-Max Scaling (Normalization) and Standardization.

'''
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Creating a sample dataset with numerical features
data = {
'Age': [20, 25, 18, 22, 3],
'TestScore': [85, 99, 78, 92, 88],
'Grade': [90, 85, 70, 95, 80]}

df = pd.DataFrame (data)
print("Original Dataset:")
print (df)

# minMax_Scaling
minMax_Scaler = MinMaxScaler()
df_standardized = minMax_Scaler.fit_transform(df)
df_standardized = pd.DataFrame(df_standardized, columns=df.columns)
print("\nAfter minMax_Scaling")
print(df_standardized)