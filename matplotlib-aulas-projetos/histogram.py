import matplotlib.pyplot as plt
import numpy as np

# representação visual da distribuicao quantitativa de dados

scores = np.random.normal(loc=80, scale = 10, size = 100)
# loc meio , scale distancia do centro, size o limite
scores = np.clip(scores,0,100)

plt.hist(scores,bins = 10 # quantidade de barras, 
                size=10,
                 color='lightgreen'
                 edgecolor = 'black') # edge color cor do contorno das barras

plt.title('Exam Scores')
plt.xlabel('Score')
plt.ylabel('# of students')

plt.show()