import numpy as np

array = np.array([[['A', 'B','C'],[ 'D','E','F',],['G','H','I']], # CADA LINHA É FEITA POR UM DICIONARIO DENTRO DE OUTRO
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'], ['Y','Z','_']]])

print(array.ndim) # DIMENSIONAL NUMEER
print(array.shape) # LINE AND COLUMNS
print(array[],[],[]) # CHAIN INDEXING [INDEX], [LINHA], [COLUNA]
print(array[][][]) # MULTIDIMENSIONAL INDEX MORE FASTER

 # filter by choice
 word = array[6,1,0], + array[1,1,0] + array[1,3,0]
 print(array)

# array[start:end:step] step negative starts from the end of array 
print(array[0:1:2])