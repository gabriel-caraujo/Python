import matplotlib.pyplot as plt
import numpy as numpy

x1 = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15,25,30,20])
y2 = np.array([35,50,55,60])

# para mais de uma linha no grafico , usar uma funcao com um dict para organizar melhor, usando no plot com **line_style
line_style = dict (marker = '.', markersize = 10,markerfacecolor = 'darkblue',markeredgecolor = '#1cd3fc',
            linestyle = 'solid',linewidth = 3,color ='#1c5bfc')

# marker muda a visualizacao dos pontos no grafico tipos em matplotlib.markers
# markersize ou ms define o tamanho do ponto
# marker face color muda a cor dos pontos, e edge color da linha podendo ser o nome da cor , RGB ou hexadecimal (colorpicker para obter os codigos das cores)
# line style muda o tipo de linha : dashed -, dot . , none so fica os pontos
# line width muda a expessura da linha
# color muda a cor da linha, mesmas regras que para os pontos 

plt.title ('Class size') # titulo do grafico

plt.xlabel('Year', fontize=20,
                    family='Arial',
                    fontweight= 'Bold',
                    color= 'Black') # titulo X
                    
plt,ylable('Students',fontize=20,
                    family='Arial',
                    fontweight= 'Bold',
                    color= 'Black') # titulo Y

plt.plot(x,y1, **line_style)
plt.plot(x,y2, **line_style)

plt.show()