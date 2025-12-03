import pandas as pd

# importar em formato csv
df = pd.read_csv('../Projetos/pokemon-pandas-matplot/data.csv')

# importar em formato json
df = pd.read_json('../Projetos/pokemon-pandas-matplot/data.json')

print(df.to_string())
