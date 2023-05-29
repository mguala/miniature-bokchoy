# -*- coding: utf-8 -*-
rut = []
ingresar = [rut.append(numeros) for numeros in raw_input("RUT ::>")]
rut.reverse()

recorrido = 2
multiplicar = 0

for x in rut:
    multiplicar += int(x) * recorrido
if recorrido == 7:
    recorrido = 1
recorrido += 1
modulo = multiplicar % 11
resultado = 11 - modulo

if resultado == 11:
    digito = 0
elif resultado == 10:
    digito = "K"
else:
    digito = resultado

print(f"Dígito verificador:", digito)
