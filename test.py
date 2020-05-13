import pandas as pd
filename = "/BulkDoownloadListing.csv"
df = pd.read_csv(filename, nrows = 20)
print(df.head())

