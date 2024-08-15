# Crear un programa para leer archivo csv

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# print(df.head())
# print(df.describe())
# print(df)
df.plot(kind = 'bar',x = 'Nombre',y = 'Edad') # Grafico de barras
plt.show()
