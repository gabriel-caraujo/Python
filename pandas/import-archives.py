import pandas as pd

# importar em formato csv
df = pd.read_csv('data.csv')

# importar em formato json
df = pd.read_json('data.json')

print(df.to_string())
