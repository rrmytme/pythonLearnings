'''
Machine learning algorithms and models only work with numerical data, Strings or categorical values must be 
converted into a numerical format. The conversion is done using some encoding techniques.
 
We'll explore three techniques for handling categorical data: 
1. One-Hot Encoding
2. Label Encoding 
3. Target Encoding

Target encoding: This encoding scheme assigns the mean or median of the target variable to each category.
Target Encoding is helpful when dealing with high-cardinality categorical variables.

Let's consider a dataset containing information about fruits, including their type and color.
'''
import pandas as pd 
from category_encoders import TargetEncoder
from sklearn.preprocessing import LabelEncoder 
# import sklearn

# Creating a sample dataset with categorical data
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana'],
    'Color': ['Red', 'Yellow', 'Orange', 'Green', 'Yellow']}

df = pd.DataFrame(data) 
print("original Dataset:") 
print(df) 

# convert the target variable 'Fruit' to numeric using LabelEncoder
label_encoder = LabelEncoder() 
df['Fruit'] = label_encoder.fit_transform(df['Fruit'])

# target_Encoding
target_encoder = TargetEncoder()
df_target_encoded = df.copy()

# Scikit-learn version 1.6 modified the API around its "tags", and that's the cause 
# AttributeError: 'super' object has no attribute '__sklearn_tags__'
# hence we commented below code and reenable this once te latest Scikit-learn version

# to see Scikit-learn installed version
# print('The scikit-learn version is {}.'.format(sklearn.__version__)) 

# df_target_encoded[['Fruit', 'Color']] = target_encoder.fit_transform(df[['Fruit', 'Color']], df['Fruit'])

# print("\nAfter target_Encoding:") 
# print (df_target_encoded)