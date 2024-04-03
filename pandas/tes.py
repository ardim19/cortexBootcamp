import pandas as pd
file = pd.read_csv("california_housing_test.csv")
file['latitude'] = file['latitude'].astype(int)
type = file.dtypes
print(type)
