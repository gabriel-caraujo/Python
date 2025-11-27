import matplotlib.pyplot as plt
import numpy as numpy

categories = np.array(['Grains', 'Fruit', 'Vegetables', 'Protein', 'Dairy', 'Sweets'])
values = np.array([5,2,6,10,3,2])

# graficos tipo barra vertical
plt.bar(categories, values, color ='darkblue')

#grafico em barra horizontal
plt.barh(categories, values, color ='darkblue')

plt.title('Daily Comsumption')
plt.xlabel('Foods')
plt.ylabel('Quantity')

plt.show()