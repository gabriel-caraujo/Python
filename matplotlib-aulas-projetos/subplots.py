import mtplotlib.pyplot as plt
import numpy as np

# figure = todo o canvas
# ax = apenas um plot (subplot) um array numpy

x = np.array([1,2,3,4,5])
figure, axes = plt.subplots(2,2) # (quantidade de linhas, quantidade de colunas)

# ax na coluna e linha 0
axes[0,0].plot(x, x*2, color='red')
axes[0,0].set_title('x*2')

# ax coluna 0 linha 1
axes[0,1].plot(x, x**2, color= 'darkblue')
axes[0,1].set_title('x**2')

# ax coluna 1 linha 0
axes[1,1].plot(x, x**3, color = 'light green')
axes[1,1].set_title('x**3')

#ax coluna 1 e linha 1
axes[1,1].plot(x, x**4, color= 'purple')
axes[1,1].set_title('x**4')


plt.tight_layout() # dimensiona as informacoes
plt.show()