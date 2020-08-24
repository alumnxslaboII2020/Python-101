"""
Tipos de datos en Python

Números: -289 123 23.12
Textos: "texto" 'texto'
Boolean: True False
Listas:
[
  True,
  "texto",
  123,
  [
    True,
    "texto",
    123, []
  ]
] 
Diccionarios:
{
  "verbo": "correr",
  "2": "dos"
}
"""

# Operaciones con números
print("\nOperaciones con números")
print(2 + 3) # 5 int
print(2 - 3) # -1 int
print(2 / 3) # 0.66666666 float
print(7 // 3) # 2 int
print(7 % 2) # 1 int
print(2 * 3) # 6 int
print(2 ** 3) # 8 int

# Operaciones con texto
print("\nOperaciones con texto")
print('Hola Pelol') # str
print("Hola " + " " + "Pelol") # concatenar texto
print("Hola" + " " + "Pelol") # concatenar texto
print("Hola"" ""Pelol") # concatenar texto

# Variables que guardan valores
hola = "Hola " # Ahora cada vez que escribimos hola, representa la cadena "Hola "
pelol = "Pelol" 

print(hola + pelol) # concatenar texto

hola = "Chau " # ahora la variable hola contiene el texto "Chau "

print(hola + pelol) # concatenar texto

print("Pelol estuvo aqui " * 5) # repetir texto
print("Pelol estuvo aqui " + str(5) + " " + "veces")

veinte = 20

print(str(veinte) + str(veinte)) # 2020
print("20" + str(veinte)) # 2020
print("Las \"comillas dobles escapadas\" tambien sirven") # repetir texto
print('Las "comillas simples" tambien sirven') # repetir texto

print("""\

  Operaciones con texto
  En muchas lineas

""")

cuarenta_y_dos = 42

print("Numero favorito: " + str(cuarenta_y_dos))
print("Numero favorito: {}".format(cuarenta_y_dos))
print(f"Numero favorito: {cuarenta_y_dos}")

# Booleanos (operadores binarios) y variables
print("\nBooleanos (operadores binarios) y variables")

print(f"Verdadero: {True}") # verdadero
print(f"Falso: {False}") # falso
print(f"Verdadero y verdadero es: {True and True}") # verdadero y verdadero = verdadero
print(f"Verdadero o verdadero es: {True or True}") # verdadero o verdadero = verdadero
print(f"Falso y verdadero es: {False and True}") # falso y verdadero = falso
print(f"Falso o verdadero es: {False or True}") # falso o verdadero = verdadero
print(f"Falso y falso es: {False and False}") # falso y falso = falso
print(f"Falso o falso es: {False or False}") # falso o falso = falso
print(f"No verdadero es: {not True}") # falso
print(f"No falso es: {not False}") # verdadero
print(f"Verdadero igual a verdadero: {True == True}") # verdadero
print(f"Falso igual a verdadero: {False == True}") # falso
print(f"Verdadero distinto de verdadero: {True != True}") # falso
print(f"Falso distinto de verdadero: {False != True}") # verdadero

# 67 esta entre 20 y 90
print(f"Se cumple que 67 > 20 y 67 < 90 {67 > 20 and 67 < 90}") # excluye 20 y 90
print(f"Se cumple que 67 >= 20 y 67 <= 90 {67 >= 20 and 67 <= 90}") # incluye 20 y 90
print(f"Se cumple que 67 > 20 y 67 <= 90 {67 > 20 and 67 <= 90}") # incluye 90 y excluye 20
print(f"Se cumple que 67 >= 20 y 67 < 90 {67 >= 20 and 67 < 90}") # incluye 20 y excluye 90

# -20 está afuera del rango 20 y 90
print(f"Se cumple que -20 < 20 o -20 > 90 {-20 < 20 or -20 > 90}") # excluye 20 y 90
print(f"Se cumple que -20 <= 20 o -20 >= 90 {-20 <= 20 or -20 >= 90}") # incluye 20 y 90
print(f"Se cumple que -20 < 20 o -20 >= 90 {-20 < 20 or -20 >= 90}") # incluye 90 y excluye 20
print(f"Se cumple que -20 <= 20 o -20 > 90 {-20 <= 20 or -20 > 90}") # incluye 20 y excluye 90

# variables para simplificar y generar consistencia
sesenta_y_siete = 67
noventa = 90

print(f"67 > 20 and 67 < 90 {sesenta_y_siete > veinte and sesenta_y_siete < noventa}") # excluye 20 y 90
print(f"67 >= 20 and 67 <= 90 {sesenta_y_siete >= veinte and sesenta_y_siete <= noventa}") # incluye 20 y 90
print(f"67 > 20 and 67 <= 90 {sesenta_y_siete > veinte and sesenta_y_siete <= noventa}") # incluye 90 y excluye 20
print(f"67 >= 20 and 67 < 90 {sesenta_y_siete >= veinte and sesenta_y_siete < noventa}") # incluye 20 y excluye 90

print(f"La variable noventa es iguala 90: {noventa == 90}") # (esto es verdadero)
print(f"La variable sesenta_y_siete es distinta de 90: {sesenta_y_siete != 90}") # (esto es verdadero)
print(f"La variable noventa es iguala 67: {noventa == 67}") # (esto es falso)
print(f"La variable sesenta_y_siete es distinta de 67: {sesenta_y_siete != 67}") # (esto es falso)

# Ejemplos de Métodos
print("\nEjemplos de Métodos")
print("estoy gritando".upper())
print("ESTOY SUSURRANDO".lower())

print("mEmE De bOB EsPonJA".swapcase())

print("Macri es un capo".replace("Macri", "Pelol"))
print("Macri es un capo".replace("capo", "gato").upper())

# Listas
# Las listas sirven para guardar elementos de cualquier tipo de manera ordenada
print("\nListas")
print([1, "dos", True, [2, "otro texto", False, []], {}])

# Las listas agrupan elementos en orden 0, 1, 2, 3,..., n - 1, siendo n la cantidad de elementos de la lista
# Las listas siempre están ordenadas
#        0, 1, 2, 3,        4
lista = [1, 2, 3, "cuatro", False]

print(f"\nLista inicial: {lista}")
print(f"Cantidad de elementos de la lista {len(lista)}") # "len" nos dice la cantidad de elementos que tiene una lista
print(f"Primer elemento de la lista {lista[0]}")
print(f"Elemento en la 4ta posicion de la lista {lista[3]}")
print(f"Elemento en la 5ta posicion de la lista {lista[4]}")

lista.append("seis") # agregar un elemento
print(f"\nLista actualizada: {lista}")
print(f"Cantidad de elementos de la lista {len(lista)}")
print(f"Elemento en la 6ta posicion de la lista de la lista {lista[5]}")

# los textos son parecidos a las listas en algunas caracteristicas
print("\nCosas en comun entre textos y listas")

cuatro = "cuatro"
cinco = "cinco"

print(f"Longitud de la variable cuatro: {len(cuatro)}") # longitud del texto "cuatro", tiene 6 caracteres
print(f"Longitud de la variable cinco: {len(cinco)}") # longitud del texto "cinco", tiene 5 caracteres
print(f"Que pasa al transformar cuatro en una lista: {list(cuatro)}") # podes transformar texto en una lista
print(f"Que pasa al transformar cinco en una lista: {list(cinco)}") # podes transformar texto en una lista

c = cuatro[0] # Podes sacar caracteres de un texto de la misma forma que elementos de una lista "c"
print(c)

# Listas adentro de listas
#                 0: [0, 1], 1: [0, 1]
matriz_cuadrada = [[1, 2], [3, 4]]

print(matriz_cuadrada)
print(matriz_cuadrada[0][0]) # pide primero el 1er elemento de la primer lista (el elemento [1, 2]) y de esa lista pide el primer elemento (1)
print(matriz_cuadrada[0][1]) # pide primero el 1er elemento de la primer lista (el elemento [1, 2]) y de esa lista pide el segundo elemento (2)
print(matriz_cuadrada[1][0]) # pide primero el 2do elemento de la primer lista (el elemento [3, 4]) y de esa lista pide el primer elemento (3)
print(matriz_cuadrada[1][1]) # pide primero el 2do elemento de la primer lista (el elemento [3, 4]) y de esa lista pide el segundo elemento (4)

# Diccionarios
# Sirven para guardar data sin necesidad de un orden específico
print("\nDiccionario")

diccionario = {
  "lista": [1, 2, 3],
  "adjetivo": "grande",
  "sustantivo": "manzana",
  "verbo": "correr",
  "numero": 42,
  "lenguajes de programacion": {
    "python": "lenguaje python",
  }
}

adjetivo = diccionario["adjetivo"]
subelemento = diccionario["lenguajes de programacion"]["python"]

print(f"Adjetivo: {adjetivo}")
print(f"Subelemento: {subelemento}")

# Tipos de datos
print("\nTipos de datos")
print(type(3))
print(type(2.2))
print(type(True))
print(type([2, 3, "hola pelol"]))
print(type({
  "hola": "pelol"
}))
print(type(type)) # el tipo de la función type
print(type(print)) # el tipo de la función print


# Ejemplo: Usuarixs de Discord

# Cada Usuarix tiene data que es cómoda de guardar en un diccionario

usuarix1 = {
  "nombre": "Usuarix 1",
  "roles": ["DJ", "admin"]
}

usuarix2 = {
  "nombre": "Usuarix 2",
  "roles": ["DJ"]
}

# En nuestro servidor, podríamos tener nuestra lista de usuarixs:
usuarixs = [usuarix1, usuarix2]