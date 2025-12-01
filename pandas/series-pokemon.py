import pandas as pd

pokemon = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Chameleon', 'Charizard']

series = pd.Series(pokemon, index=['1','2', '3','4','5','6'])

print(series)

