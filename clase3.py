from scipy.io.wavfile import read # libreria para lectura de archivos de audio
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio # para escuchar la senal

#Importa una señal de audio y encuentra la energía

def logEnergy(senal2): # Definir la funcion
    sig2=np.square(senal2) # Elevar al cuadrado las muestras de la senal
    sumsig2=np.sum(sig2) # Sumatoria
    logE=10*np.log10(sumsig2) # Convertir a dB
    dc=np.mean(senal2) # Promedio
    return logE, dc

file_audio=('senal.wav') # Ruta del archivo con la senal
fs, x=read(file_audio) # Cargar el archivo
x=x/float(max(abs(x))) # escala la amplitud de la senal
t=np.arange(0, float(len(x))/fs, 1.0/fs) # Vector de tiempo
plt.plot(t,x) # Dibujar la grafica
# Los siguientes dos comandos dibujan las etiquetas de los ejes
plt.xlabel('Time',fontsize=18) # Etiqueta eje X
plt.ylabel('Amplitude',fontsize=18) # Etiqueta eje Y
plt.show() # Mostrar la grafica
#Audio(x, rate=fs) # para escuchar la senal, si se desea

Energy, DCvalue = logEnergy(x)
print('Energia='+str(Energy))
print('Valor DC='+str(DCvalue))

