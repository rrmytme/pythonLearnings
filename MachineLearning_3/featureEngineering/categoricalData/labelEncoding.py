'''
Machine learning algorithms and models only work with numerical data, Strings or categorical values must be 
converted into a numerical format. The conversion is done using some encoding techniques.
 
We'll explore three techniques for handling categorical data: 
1. One-Hot Encoding
2. Label Encoding 
3. Target Encoding

Label encoding: The label encoding technique assigns a respective integer value to each categorical variable.
Label Encoding is of use when the categorical features have an ordinal relationship.

Let's consider a dataset containing information about fruits, including their type and color.
'''
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 

# Creating a sample dataset with categorical data
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana'],
    'Color': ['Red', 'Yellow', 'Orange', 'Green', 'Yellow']}

df = pd.DataFrame(data) 
print("original Dataset:") 
print(df) 

label_encoder = LabelEncoder() 
df_label_encoded = df.copy()
df_label_encoded['Fruit'] = label_encoder.fit_transform(df['Fruit'])
df_label_encoded['Color'] = label_encoder.fit_transform(df['Color'])

print("\nAfter label Encoding:") 
print (df_label_encoded)