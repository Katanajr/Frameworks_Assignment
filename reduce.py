import pandas as pd

# Load only first 5000 rows
df = pd.read_csv("metadata.csv", nrows=5000)

# Save as sample file
df.to_csv("metadata_sample.csv", index=False)
