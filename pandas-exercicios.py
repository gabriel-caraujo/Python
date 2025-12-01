import pandas as pd

data = [100,102,104]


## Series = a pandas 1 dimensional labeled array that can hold any data type
# think of it like a single column in a spreadsheet (1 dimensinal)
series = pd.Series(data, index=['a', 'b', 'c'])

print(series)
