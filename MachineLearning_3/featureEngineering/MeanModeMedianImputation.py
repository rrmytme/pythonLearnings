#Fill missing data using Mean/Median/Mode
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
'Name': ['John', 'Alice', 'Bob', 'Emma', 'Ton'],
'Age': [20, np.nan, 22, 19, 18],
'TestScore': [85, 99, np.nan, 78, 921],
'Grade': ['A', 'B', np.nan, 'C', 'A']
}

df = pd.DataFrame(data)
print("\nBefore the Mean/Median Tmputation:")
print(df)

imputer = SimpleImputer(strategy='mean') # Other strategies: 'median', 'most frequent' for mode
df_imputed = pd.DataFrame(imputer.fit_transform(df[['Age', 'TestScore']]), columns=['Age', 'TestScore'])
df['Age'] = df_imputed['Age']
df['TestScore'] = df_imputed['TestScore']

print("\nafter the Mean/Median Tmputation:")
print(df)