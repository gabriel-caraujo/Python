import pandas as pd

df = pd.read_csv('data.csv')

#ALL DATAFRAME
'''
média print(df.mean(numeric_only=True))
soma print(df.sum(numeric_only=True))
min print(df.min(numeric_only=True))
max print(df.max(numeric_only=True))
contar print(df.count())
'''
#SINGLE COLUMN
'''
média print(df['Height'].mean())
soma print(df['Height'].sum())
min print(df['Height'].min())
max print(df['Height'].max())
contar print(df['Height'].count())
'''
#AGRUPAR
group = df.groupby('Type1')
''' 
print(group['Height'].mean())
print(group['Height'].sum())
print(group['Height'].min())
print(group['Height'].max())
print(group['Height'].count())
'''
