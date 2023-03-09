#mostrar en graficos las operacion entre señales: escalamiento


import numpy as np
import matplotlib.pyplot as plt
import math 

f=1.0 # Frecuencia de la senal
fs=7*5.0 # Frecuencia de muestreo
t=np.arange(0, 2.0, 1.0/fs) # Vector de tiempo
x = np.sin(2*np.pi*f*t)
#señal original 
plt.subplot(1, 2, 1)
plt.plot(t,x)
plt.xlabel('Time',fontsize=10)
plt.ylabel('Amplitude',fontsize=10)

x = 3*np.sin(2*np.pi*f*t)
#señal escalada 
plt.subplot(1, 2, 2)
plt.plot(t,x)
plt.xlabel('Time',fontsize=10)
plt.ylabel('Amplitude',fontsize=10)
plt.show()

