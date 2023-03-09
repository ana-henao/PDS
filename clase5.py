#convolucion de secuencias
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

xn=[-2,0,1,-1,3] #secuencia 1 x(n)
h_n=[1,2,0,-1]#secuencia 2 h(n)
#h_k=[-1,0,2,1] #secuencia h(-k): secuencia h_n con sus posiciones invertidas

print('secuencia x(n): '+ json.dumps(xn))
print('secuencia h(k): '+ json.dumps(h_n))

def convolucion(xn, hn):
    #Encontrar Rango
    a=len(xn)-1+len(hn)-1
    
    #Agregar ceros
    b_x=len(xn)
    dif=abs(a-b_x)
    vect_x=np.zeros(dif+1)
    x_=np.concatenate((xn,vect_x), axis=0)
    x_n=list(x_)
    
    b_h=len(hn)
    dif=abs(a-b_h)
    vect_h=np.zeros(dif+1)
    h_=np.concatenate((h_n,vect_h), axis=0)
    h_k=list(h_)

    #Calcular Convolución
    y =[]
    for lim in range(1,(len(x_n)+len(h_n))-3):
        n=0;
        mult=[]
        for i in range(lim,0,-1): #para xs        
            mult.append(x_n[i-1]*h_k[n])
            n+=1

        suma=0
        for j in mult:
            suma+=j

        y.append(suma)
        
    return y


y = convolucion(xn,h_n)
print('y(n): '+json.dumps(y))

figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("X[n]")
plt.stem(xn)

plt.subplot(1, 3, 2)
plt.title("h[n-k]")
plt.stem(h_n)

plt.subplot(1, 3, 3)
plt.title("y[n] - Convolución")
plt.stem(y)
plt.show()
    
    
