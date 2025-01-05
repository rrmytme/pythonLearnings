'''
Machine learning algorithms and models only work with numerical data, Strings or categorical values must be 
converted into a numerical format. The conversion is done using some encoding techniques.
 
We'll explore three techniques for handling categorical data: 
1. One-Hot Encoding
2. Label Encoding 
3. Target Encoding

One-hot encoding: The categorical variables are converted or transformed into binary(0 and 1) vectors 
assigned as a separate feature to the dataset. One-Hot Encoding is suitable when the categorical 
features do not have a natural order.


Let's consider a dataset containing information about fruits, including their type and color.
'''
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder  

# Creating a sample dataset with categorical data
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana'],
    'Color': ['Red', 'Yellow', 'Orange', 'Green', 'Yellow']}

df = pd.DataFrame(data) 
print("original Dataset:") 
print(df) 

# 1. One-Hot Encoding 
one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first') #We dropped the first category to avoid multicollinearity issues.
one_hot_encoded = one_hot_encoder.fit_transform(df[['Fruit', 'Color']])
feature_names = one_hot_encoder.get_feature_names_out(['Fruit', 'Color'])
df_one_hot = pd.DataFrame(one_hot_encoded, columns=feature_names) 

# Concatenate the encoded DataFrame with the original DataFrame
df_encoded = pd.concat([df.drop(['Fruit', 'Color'], axis=1), df_one_hot], axis=1) 
print("\nAfter One-Hot Encoding:") 
print (df_encoded)