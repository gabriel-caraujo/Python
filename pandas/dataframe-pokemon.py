import pandas as pd

pokemon = { 'Nome': ['Bulbasaur', 'Pikachu', 'Snorlax', 'Charmander', 'Cubone', 'Gengar'],
            'Type': ['Grass', 'Electric', 'Normal', 'Fire','Ground', 'Poison'],
}

df = pd.DataFrame(pokemon, index=['102','55','250', '239', '226', '261'])

print(df)
