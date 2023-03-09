#transformada z de funcion 
import sympy

s, z = sympy.symbols('s, z') #Declaración de z como simbolo 
k = sympy.Symbol('k', integer=True)# Declaración de k como simbolo entero

Amp = 1
#Rampa Unitaria -> 1 * k * z**-k
#Limites -> k esta entre 0 e infinito
rampaUnitaria = sympy.Sum(Amp * k * z**-k, (k, 0, sympy.oo))
shortform = rampaUnitaria.doit() #Resolución de Sumatoria

uz = shortform.args[0][0]
roc = shortform.args[0][1]

print(f"Resultado Sumatoria: \n {uz}")
print(f"ROC: \n {roc}")
