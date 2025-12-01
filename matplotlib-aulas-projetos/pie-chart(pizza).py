import matplotlib.pyplot as plt
import numpy as np

categories = ['Freshmen', 'Juniors', 'Sophomores', 'Seniors']
values = np.array([300, 260, 350, 480])

# comando para grafico de pie
plt.pie(values, labels=categories,
                autopct= '%1.1f%%' # diminuir numero de casas decimais
                explode=[0,1,0,1] # criar espaço entre uma parte e as demais 0 sem espaço, 1 para cima aumenta o espaço
                startangle= 90) # angulo de inicio do grafico
plt.title('Students')
plt.show()