# extenciones 1. python 2. python extension pack 3. python debugger
# Crear un programa para ller un archivo de texto
with open('textoparaclase3.txt','r')as arc: # incializamos lectura de archivo,  arc es una variable donde se guardara el contenido del archivo de texto
    content = arc.read()

print('El contenido dle archivo es: ', content)

