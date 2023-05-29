def hacer_grandioso(lista):
    for i in range(len(lista)):
        if lista[i] in ['Harry Houdini', 'David Blaine', 'Teller']:
            lista[i] = 'El gran ' + lista[i]

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Lista original de nombres
nombres = [
    'Harry Houdini',
    'Newton',
    'David Blaine',
    'Hawking',
    'Messi',
    'Teller',
    'Einstein',
    'Pele',
    'Juanes'
]

# Imprimir la lista completa de nombres antes de ser modificados
print("Lista completa de nombres:")
imprimir_nombres(nombres)

# Separar en grupos: magos, científicos y otros
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

# Modificar la lista de magos añadiendo 'El gran' antes del nombre
hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos
print("\nMagos grandiosos:")
imprimir_nombres(magos)

# Imprimir los nombres de los científicos
print("\nCientíficos:")
imprimir_nombres(cientificos)

# Imprimir los nombres restantes (otros)
print("\nOtros:")
imprimir_nombres(otros)