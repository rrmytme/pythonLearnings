'''
Feature Scaling is a method of feature engineering that involves transforming features. 
The features are transformed into floats within a boundary of values, usually between 0 and 1. 
The features, being within the same boundary have none dominating the other.

Standardization: Standardization converts the features in a dataset using the mean and standard deviation. 
The value of the mean is 0 and the standard deviation is 1.

Let's consider a dataset that contains information about students, including their age, test scores, and 
grades. We will demonstrate two feature scaling techniques: Min-Max Scaling (Normalization) and Standardization.

'''
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Creating a sample dataset with numerical features
data = {
'Age': [20, 25, 18, 22, 3],
'TestScore': [85, 99, 78, 92, 88],
'Grade': [90, 85, 70, 95, 80]}

df = pd.DataFrame (data)
print("Original Dataset:")
print (df)

# 2. Standardization
standard_scaler = StandardScaler()
df_standardized = standard_scaler.fit_transform(df)
df_standardized = pd.DataFrame(df_standardized, columns=df.columns)
print("\nAfter Standardization:")
print(df_standardized)