import math
import numpy as np
import matplotlib.pyplot as plt

lejos = 15


x_1 = [n for n in range(lejos)]


y_1 = [1/math.factorial(n) for n in range(lejos)]
y_5 = [(5**n)/math.factorial(n) for n in range(lejos)]
y_6 = [(6**n)/math.factorial(n) for n in range(lejos)]
y_7 = [(7**n)/math.factorial(n) for n in range(lejos)]
y_10 = [(10**n)/math.factorial(n) for n in range(lejos)]

#plt.scatter(x_1,y_1)
plt.scatter(x_1,y_5,label = "5")
plt.scatter(x_1,y_6,label = "6")
plt.scatter(x_1,y_7,label="7")
#plt.scatter(x_1,y_10,label="10")
plt.legend() #Si no pongo Legend no puedo configurar las opciones label
plt.grid(True,axis="x") #axis puede ser "x","y","both"
plt.show()