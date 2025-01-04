#Fill missing data using Forward or Backward row data 
import pandas as pd
import numpy as np

data = {
'Name': ['John', 'Alice', 'Bob', 'Emma', 'Ton'],
'Age': [20, np.nan, 22, 19, 18],
'TestScore': [85, 99, np.nan, 78, 921],
'Grade': ['A', 'B', np.nan, 'C', 'A']
}

df = pd.DataFrame(data)

print("\nBefore Forward Fill/Backward Fill Imputation")
print(df)

dfForwardFill = df.ffill(inplace=True)
print("\nafter the Forward Fill Tmputation:")
print(df)

dfBackwardFill = df.bfill(inplace=True)
print("\nafter the Backward Fill Tmputation:")
print(df)