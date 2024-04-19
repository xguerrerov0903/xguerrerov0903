import numpy as np

import matplotlib.pyplot as plt

def crear_matriz(filas, columnas):
    # Genera una matriz de dimensiones filas x columnas con valores aleatorios de 0 y 1
    matriz = np.random.randint(2, size=(filas, columnas))
    return matriz


def mostrar_nonograma(matriz):
    plt.imshow(matriz, cmap='binary', interpolation='nearest')
    plt.grid(True, color='gray', linewidth=1)  # Agrega una cuadrícula con color rojo y ancho de línea 2
    
    # Configura las marcas en los ejes x e y para que estén alineadas con los bordes de las celdas
    plt.xticks(np.arange(-0.5, len(matriz[0]), 1), [])
    plt.yticks(np.arange(-0.5, len(matriz), 1), [])
    
    plt.show()

def numeros_claves (matriz):
    lista_claves = []
    for x in matriz:
        num_clave = []
        numero = 0
        for y in x:
            if y == 1:
                numero += 1
            else:
                if numero > 0:
                    num_clave.append(numero)
                    numero = 0
        if numero > 0:
            num_clave.append(numero)
        lista_claves.append(num_clave)
    return lista_claves


filas = int(input("Ingresa las filas (horizontales): "))
columnas = int(input("Ingresa las columnas (verticales): "))
matriz_aleatoria = crear_matriz(filas, columnas)

claves_columna = numeros_claves(matriz_aleatoria)

matriz_filas = list(zip(*matriz_aleatoria))

claves_filas = numeros_claves(matriz_filas)

print(matriz_aleatoria)

print(claves_columna)
print(claves_filas)
mostrar_nonograma(matriz_aleatoria)