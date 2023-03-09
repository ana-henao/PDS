#librerias 
from cmath import log
import numpy as np
import matplotlib.pyplot as plt
#se toman temperaturas  y se muestra en un grafco la variacion diaria 

vect=[]#vector de temperatura
m=50

for i in range(m):
    vect.append(log(i/m,10)) 
t=np.linspace(1,10,m, dtype=int)

#Gráfico de las temperaturas promedio diarias en el mes de enero en la ciudad
plt.figure()
plt.plot(t, vect, 'b', label = 'Variacion de la temperatura')
plt.title("Variacion de la temperatura en el mes de enero durante 10 dias.")
plt.xlabel('Tiempo')
plt.ylabel('Variacion Temperatura')
plt.grid()
plt.legend()
plt.show()