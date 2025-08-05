import pandas as pd

# Load the dataset
df = pd.read_csv('app/model-training/heart_disease_uci.csv')

# Display the first few rows of the dataframe
print(df.head())

# Display basic information about the dataframe
print(df.info())

# Display descriptive statistics of the dataframe (mean, min, max, etc.)
print(df.describe())

# Display the unique values in the 'num' column
print("Unique values in 'num':", df['num'].unique())