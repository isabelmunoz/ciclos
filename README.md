# ciclos

## Requerimientos
El siguiente desafío presenta 4 casos en los que se requiere emplear Ciclos para su
resolución:
1. Primeros Auxilios (3 Puntos)
2. Filtrado Compacto (1 Punto)
3. Fuerza Bruta (3 Puntos)
4. Módulo 11 (3 Puntos)
Cada desafío presentará requerimientos independientes de modo de obtener un programa
con su resolución.

## Primeros Auxilios
En cualquier momento puede haber una emergencia y hay que estar preparados ¿sabrías
cómo reaccionar en caso de que alguien necesite de primeros auxilios?
Es muy probable que mucha gente no conozca cuáles son los pasos a seguir en caso de
emergencia. Es por eso que se le solicita construir una aplicación que permita indicar los
pasos a seguir ante una emergencia. Debido a que no se espera que usted sea un experto en
el tema se le provee de un diagrama que explica las distintas instancias a la que se está
sometido durante una emergencia.

![image](https://user-images.githubusercontent.com/36016296/166113535-1c3454d7-61b2-4219-92db-838ab46254ef.png)


Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
en tiempo real.


## Filtrado compacto
Una empresa provee de los balances del año anterior en un diccionario como se muestra a
continuación:

![image](https://user-images.githubusercontent.com/36016296/166113580-6ff2981d-3b08-4f32-addf-71ed25b0f3e7.png)


Se solicita devolver un informe resumido que exponga los meses que superan un cierto
umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor
asociado siempre y cuando superen el umbral especificado.

Ejemplo:

![image](https://user-images.githubusercontent.com/36016296/166113602-f6668420-53a7-4c24-904b-dd6c95381b66.png)


## Fuerza bruta
¿Qué tan seguro es tu password? ¿Intentemos hackear un password? Mediante el siguiente
desafío se busca utilizar un algoritmo muy sencillo, llamado fuerza bruta para determinar
cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula.
Para ello se ingresará un password oculto. Este password puede contener sólo
combinaciones de letras y se requiere determinar su seguridad. Un mayor número de
intentos implica un password más seguro:

El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en
orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña
indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.

Consideraciones
-  Utilizar from string import ascii_lowercase
- ascii_lowercase es un string con todas las letras del abecedario en minúsculas (sin la ñ).
- No considerar la ñ.
- Considera mayúsculas y minúsculas como una misma letra.
- Se considera "intento" cada vez que se compara una letra.

Ejemplo:
○ Usuario ingresa "abc"
○ El computador compara:
- ■ a es igual a a => Sí (1 intento), continúa con la siguiente letra.
- ■ b es igual a a => No (2 intentos), prueba otra comparación.
- ■ b es igual a b => Sí (3 intentos), continúa con la siguiente letra.
- ■ c es igual a a => No (4 intentos), prueba con otra comparación.
- ■ c es igual a b => No (5 intentos), prueba con otra comparación.
- ■ c es igual a c => Sí (6 intentos), continúa con la siguiente letra.
- ■ No hay más letras. Se adivinó la palabra en 6 intentos.

NOTA: A modo explicativo se mostrará la contraseña a buscar pero la idea es que ésta se
ingrese de manera oculta.

![image](https://user-images.githubusercontent.com/36016296/166113646-ae8652d1-a95a-4c76-8dd0-8a969b753775.png)


## Módulo 11
Módulo 11 es un algoritmo con el cual se calcula el dígito verificador (o DV, es el número que
va después del guión), para los RUT en chile. Este número evita que cualquier persona pueda
inventar un RUT aleatoriamente.

Se pide crear un programa en Python llamado dv.py que permita ingresar el número de RUT
sin puntos ni DV y devuelva el DV correspondiente.
Para ello se provee un ejemplo de cálculo, una especie de pseudo código que explica su
funcionamiento:

- ● Dado el RUT 12 345 678-5.
- ● Llamaremos Número a 12 345 678 y Dígito Verificador (DV) a 5

1. Se toma la siguiente serie numérica: 2, 3, 4, 5, 6, 7.
2. Se multiplicará cada dígito del Número por su correspondiente en la serie numérica,
partiendo desde el final del número. En caso de tener más números en la serie
numérica, ésta se reinicia.
3. Ejemplo de Multiplicación

![image](https://user-images.githubusercontent.com/36016296/166113681-ea284b68-fe4b-4598-ade5-6994be856cc2.png)

4. La suma de cada todas las multiplicaciones es: 16+21+24+25+24+21+4+3 = 138
5. El siguiente paso es aplicar el módulo 11 (por esto se llama módulo 11). Sólo se
toma en cuenta el cociente entero.
6. 138 / 11 = 12 el resto (o módulo) es 6, ya que 11*12 + 6 es 138.
7. Para calcular el dígito verificador se resta el resto (6) a 11, lo cual es: 11 - 6 = 5
8. Finalmente se aplican las reglas del algoritmo:
○ Si el resultado es igual a 10, el DV es K
○ Si el resultado es 11, el DV es cero,
○ En cualquier otro caso, no se modifica.
9. En este caso el DV sigue siendo 5.

Se puede verificar el correcto funcionamiento del programa ingresando su propio número de
RUT. El programa se espera que funcione de la siguiente manera:

![image](https://user-images.githubusercontent.com/36016296/166113701-6b376e1a-e24b-4aa2-b635-46eaad4118dd.png)

