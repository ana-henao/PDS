#diagrama de polo y cero
import control
import matplotlib.pyplot as plt
from numpy import real, imag
from control.grid import zgrid

#Se hace uso de la librería control para generar la función de transferencia
tf = control.tf([1,0],[1,0.25,-0.25],True)

print(f"Z Transfer function -> {tf}")

#Se extraen con la librería control los polos y ceros
poles = tf.poles()
zeros = tf.zeros()

#Se usa la función zgrid de la libreria control para los ejes y características de la grafica
ax, fig = zgrid()
ax.scatter(real(poles), imag(poles), s=50, marker='x',
                       facecolors='k')
ax.scatter(real(zeros), imag(zeros), s=50, marker='o',
                       facecolors='none', edgecolors='k')
plt.title("Polos y Ceros")
plt.show()

