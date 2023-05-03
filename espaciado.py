def ConvertirEspaciado(texto):
    # Inicializar una cadena vacía para almacenar el resultado
    resultado = ""

    # Iterar sobre cada letra en el texto
    for letra in texto:
        # Agregar la letra actual al resultado
        resultado += letra
        # Agregar un espacio después de la letra actual
        resultado += " "

    # Devolver el resultado
    return resultado

# Pedir al usuario que ingrese un texto
texto = input("Ingrese un texto: ")

# Llamar a la función ConvertirEspaciado y mostrar el resultado
print("Texto con espaciado adicional: ", ConvertirEspaciado(texto))
