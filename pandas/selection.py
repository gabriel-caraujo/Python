import pandas as pd

# importar em formato csv
#df = pd.read_csv('data.csv')

#mudar index do arquivo
df = pd.read_csv('../Projetos/pokemon-pandas-matplot/data.csv', index_col='Name')

# solicitando o dado a ser procurado
pokemon = input ('enter a Pokemon name: ')

try:
    print(df.loc[pokemon])
except KeyError:
    print(f'{pokemon} not found')

# selecionar por coluna
#print(df['Name'].to_string())

# selecionar mais de uma coluna
#print(df[['Name', 'Height', 'Weight']].to_string())

# selecionando linha com mais de uma coluna
#print(df.loc['Mewtwo', ['Height', 'Weight']])

# selecionando um intervalo de linhas
#print((df.loc['Pikachu': 'Snorlax']))


