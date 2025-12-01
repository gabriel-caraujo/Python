import numpy as np

# Scalar arithmetic

array = np.array([1,2,3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print (array ** 5)

#  comparison operators
scores = np.array([91,55,100,73,82,64])
print(scores == 100) # equal
scores [scores < 60 = 0] # less than 60 change value to 0
print(scores)
# vectorized math funcs

print(np.sqrt(array))
print(np.round(array)) # FLOOR TO DOWN , CEIL TO UPPER

# EXERCISE

radii = np.array([1,2,3])
print(np.pi * radi ** 2) 