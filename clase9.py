#transformada z inversa
from lcapy.discretetime import z

#Se hace uso de la libreria lcapy para el manejo de funciones en transformada z
zfuntion=(z**3)/((z+1)*(z-1)**2)
print(f"\nFuncion en transformada z : {zfuntion}")

#De la libreria lcapy se realizar la transformada inversa
xk=zfuntion.IZT()

print(f"\nResultado Transformada Inversa :{xk.args[0][0]}")
print(f"\nCondiciones:{xk.args[0][1]}")