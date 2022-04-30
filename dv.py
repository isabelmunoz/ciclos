rut = []
ingresar = [rut.append(numeros) for numeros in input('Ingresa tu RUT sin puntos ni digito verificador: ')]
rut.reverse()
print(rut)
recorrido = 2
multiplicar = 0

for x in rut:
    multiplicar += int(x)*recorrido
    recorrido += 1
    if recorrido >= 8:
        recorrido = 2
    print(multiplicar)
modulo = multiplicar % 11
resultado = 11-modulo
if resultado == 11:
    digito = 0
elif resultado == 10:
    digito = "K"
else:
    digito = resultado
print("Su dígito verificador es :",digito)