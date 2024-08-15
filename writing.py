# programa para escribir contenido en un archivo

texto = "Esta es una prueba para escribir texto dentro de un archivo"

with open('texto.txt', 'w') as arc:
    arc.write(texto)

print('archivo escrito correctamente')