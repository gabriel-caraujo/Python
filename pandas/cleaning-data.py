import pandas as pd

df = pd.read_csv('../Projetos/pokemon-pandas-matplot/data.csv')

# drop irrelevant columns
df.drop(columns=['Legendary'])

# Handle missing data
df = df.dropna(subset=['Type2'])
df  = df.fillna({'Type2' : 'none'})

# fix inconsistents values
df['Type1'] = df['Type1'].replace({'Grass' : 'GRASS'})

# Standardize text
df['Name'] = df['Name'].str.lower()

# data types
df['Legendary'] = df['Legendary'].astype(bool)

# removing duplicate
df = df.drop_duplicates()
