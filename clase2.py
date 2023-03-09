import numpy as np
import matplotlib.pyplot as plt # libreria usada para graficas
#Muestreado de las señales cumpliendo el teorema de nyquist
f=1.0 # Frecuencia de la senal
fs=5.0 # Frecuencia de muestreo
t=np.arange(0, 2.0, 1.0/fs) # Vector de tiempo
x = np.sin(2*np.pi*f*t)
plt.subplot(1, 2, 1)
plt.plot(t,x)
plt.xlabel('Time',fontsize=10)
plt.ylabel('Amplitude',fontsize=10)


fs2=30.0 # Frecuencia de muestreo 2 (con teorema nyquist)
t=np.arange(0, 2.0, 1.0/fs2) # Vector de tiempo
x = np.sin(2*np.pi*f*t)
plt.subplot(1, 2, 2)
plt.plot(t,x)
plt.xlabel('Time',fontsize=10)
plt.ylabel('Amplitude',fontsize=10)
plt.show()