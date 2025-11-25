import pandas as pd

# importar em formato csv
df = pd.read_csv('data.csv')

#tall_pokemon = df[df['Height'] >= 2]

#legendary_pokemon = df[df['Legendary'] == True]

#water_pokemon = df[(df['Type1'] == 'Water') or (df['Type2'] == 'Water')]

#ff_pokemon = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]

print(df.to_string())
