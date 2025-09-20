import pandas as pd
df = pd.read_csv("metadata-sample.csv")
print(df.shape)       # rows and columns
print(df.info())      # data types
print(df.head())      # first few rows
print(df.isnull().sum())  # missing values