import string

password = input('Ingrese la contraseña')
abc = string.ascii_lowercase
contador_intentos = 0

for caracter in password:
    for cont in abc:
        if caracter == cont:
            contador_intentos = contador_intentos + 1
            break
        else:
            contador_intentos = contador_intentos + 1

print(f'La contraseña fue forzada en {contador_intentos} intentos')