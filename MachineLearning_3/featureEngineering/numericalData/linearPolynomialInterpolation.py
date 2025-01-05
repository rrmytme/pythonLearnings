#his is the process of estimating and filling in missing values using techniques like linear or polynomial interpolation.
#for ex: 10, nan, 30 -> interpollation would be 10 + 30 /2 = 20 
import pandas as pd
import numpy as np

data = {
'Name': ['John', 'Alice', 'Bob', 'Emma', 'Ton'],
'Age': [20, np.nan, 22, 19, 18],
'TestScore': [85, 99, np.nan, 78, 92],
'Grade': ['A', 'B', np.nan, 'C', 'A']
}

df = pd.DataFrame(data)

print("\nBefore Interpollation")
print(df)
df.infer_objects(copy=False)
dfInterpolated = df.interpolate()
print("\nafter Interpollation")
print(dfInterpolated)