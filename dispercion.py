import numpy as np
import matplotlib.pyplot as plt

# generar una lista con 100 numeros aleatorios para el eje x
x = np.random.rand(100)
# print(x)

#Genera una lista con 100 numeros aleatorios para el eje y
y = np.random.rand(100)

# Visualizar un diagrama de dispersion
plt.scatter(x,y)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()