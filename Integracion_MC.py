import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

cantidad = 1000000
xy = [[rd.random(),rd.random()] for j in range(cantidad)]

def f(pto):
    return pto**2


positivos = 0
integrales = []
cantidad = []
for j,x in enumerate(xy):
    if x[0] < f(x[1]):
        positivos += 1
    
    if ((j%10000) == 0) and (j != 0):
        integrales.append(positivos / j )
        cantidad.append(j)

plt.scatter(cantidad,integrales)
plt.plot([1,1000000],[1/3,1/3],c="r")
plt.show()
print(integrales[-1])
