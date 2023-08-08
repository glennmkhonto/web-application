import pandas as pd

# Read the CSV file
df = pd.read_csv('csv/tests.csv')

# Get the column names
columns = df.columns.tolist()

print(columns)
