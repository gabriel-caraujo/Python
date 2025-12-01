import matplotlib.pyplot as plt
import numpy as np

# mostrar o relacionamento entre duas variaveis

x1= np.array([0,1,1,2,3,4,5,6,7,7,8]) # hours studied
y1 = np.array([55,60,65,62,68,70,75,78,82,85,95]) # grade

x2= np.array([0,1,2,2,3,4,5,6,7,7,8,8]) # hours studied
y1 = np.array([50,58,65,70,72,78,83,88,92,95,97]) # grade

plt.scatter(x1,y1, color='skyblue',
                  alpha = 0.5 # transparencia dos pontos
                  s = 200 # tamanho da esfera
                  label='Class A')

plt.scatter(x2,y2, color='red',
                  alpha = 0.5 # transparencia dos pontos
                  s = 200 # tamanho da esfera
                  label = 'Class ')

plt.title('Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')

plt.legend() # mostrar o nome class da label
plt.show()