import random
import numpy as np

def generar_lista_aleatoria(n):
    return [random.randint(0, 100) for i in range(n)]

def calcular_media(muestra):
    suma = 0
    n = len(muestra)
    for i in range(n):
        suma += muestra[i]
    media = suma / n
    return media

def calcular_estadisticas(muestra):
    media = calcular_media(muestra)
    varianza = np.var(muestra, ddof=1)
    desviacion_estandar = np.std(muestra, ddof=1)
    return {'media': media, 'varianza': varianza, 'desviacion_estandar': desviacion_estandar}

n = int(input("Ingrese el tamaño de la muestra: "))
lista_aleatoria = generar_lista_aleatoria(n)
estadisticas = calcular_estadisticas(lista_aleatoria)
print(estadisticas)
print("La lista aleatoria es:", lista_aleatoria)