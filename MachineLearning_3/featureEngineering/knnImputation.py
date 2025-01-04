#Fill in missing data using the features derived from using the KNN(K- Nearest Neighbors) algorithm on the other features of the dataset.
#for ex: 10, nan, 30, 40 -> KNNImputer would be 10 + 30 + 40 /3 = 26.66 
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

data = {
'Name': ['John', 'Alice', 'Bob', 'Emma', 'Ton'],
'Age': [20, np.nan, 22, 19, 18],
'TestScore': [85, 99, np.nan, 78, 92],
'Grade': ['A', 'B', np.nan, 'C', 'A']
}

df = pd.DataFrame(data)

print("\nBefore KNNImputation")
print(df)
knnImputerAge = KNNImputer(n_neighbors=3)
df['Age'] = knnImputerAge.fit_transform(df[['Age']])

knnImputerTestScore = KNNImputer(n_neighbors=3)
df['TestScore'] = knnImputerTestScore.fit_transform(df[['TestScore']])

print("\nafter KNNImputation")
print(df)