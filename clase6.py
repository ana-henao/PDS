#Correlación entre dos secuencias
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

xn=[0,0,2,-1,3,7,1,2,-3,0,0] #secuencia 1 x(n)
xn_0 = 6
h_n=[0,0,1,-1,2,-2,4,1,-2,5,0]#secuencia 2 h(n)
hn_0= 6
#h_k=[-1,0,2,1] #secuencia h(-k): secuencia h_n con sus posiciones invertidas

print('secuencia x(n): '+ json.dumps(xn))
print('secuencia h(k): '+ json.dumps(h_n))

def correlacion(x_n, h_k, xn_0, hn_0):
    #Calcular correlacion
    x_f = x_n
    y =[]
    m =0
    for lim in range(0,(len(x_n)+len(h_k))):
        mult=[]
        print(f"lim : {lim}")
        
        part1 = []
        if(m<=xn_0+1):
            for i in range(0,len(x_n)): #para xs 
                print('secuencia x(n): '+ json.dumps(x_f))
                print('secuencia h(k): '+ json.dumps(h_k))
                print(f"x_n : {x_f[i]} - h_k : {h_k[i]}")
                print(f"mult:{x_f[i]*h_k[i]}")
                mult.append(x_f[i]*h_k[i])

            temp = x_f[len(x_f)-1]    
            x_f=x_f[:-1]     
            x_f.insert(0,0)
            m+=1
        else:
            mult.reverse()
            for i in range(0,len(x_n)): #para xs 
                print('secuencia x(n): '+ json.dumps(x_n))
                print('secuencia h(k): '+ json.dumps(h_k))
                print(f"x_n : {x_n[i]} - h_k : {h_k[i]}")
                print(f"mult:{x_n[i]*h_k[i]}")
                mult.append(x_n[i]*h_k[i])
            m+=1
            temp = h_k[len(h_k)-1]    
            h_k=h_k[:-1]     
            h_k.insert(0,0)

        suma=0
        for j in mult:
            suma+=j
        print(f"suma: {suma}")
        y.append(suma)
        y[0]=0
        print("-----Mov-------")
        
    return y
y = correlacion(xn,h_n,xn_0,hn_0)
print('y(n): '+json.dumps(y))

figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("X[n]")
plt.stem(xn)

plt.subplot(1, 3, 2)
plt.title("h[n-k]")
plt.stem(h_n)

plt.subplot(1, 3, 3)
plt.title("y[n] - Correlación")
plt.stem(y)
plt.show()