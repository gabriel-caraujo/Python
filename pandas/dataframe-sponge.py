import pandas as pd

data = {
    'Nome': ['Bob esponja', 'Patrick', 'Lula molusco'],
    'Idade': [18,16,25]
}

df = pd.DataFrame (data, index=['Empregado 1 ', 'Empregado 2', 'Empregado 3'])

# Adicionando nova coluna

df['Ocupação'] = ['Cozinheiro', 'N/A', 'Caixa']

# adicionando novas linhas

nova_linha = pd.DataFrame([{'Nome': 'Sandy', 'Idade': 20, 'Ocupação': 'Engenheira'},
                          {'Nome': 'Seu sirigueijo', 'Idade': 60, 'Ocupação': 'Gerente'}], index=['Empregada 4', 'Empregado 5'])
df = pd.concat([df,nova_linha])

print(df)
