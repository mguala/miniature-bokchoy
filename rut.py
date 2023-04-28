rut = reversed(input('ingresa tu RUT::>')) #reversa el rut al input

d = sum([int(n)*list(range(2,8))[i%6] for i,n in enumerate(rut)]) #inside out -> mueve el index del input a la vez que mueve el index del range 2,8

d %= 11 //divide por 11

if (d==1):
    d = 'K'
else:
    d = 11-d
    
print(d)
