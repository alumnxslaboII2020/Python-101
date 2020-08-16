"""
Tipos de datos en Python

Números: -289 123 23.12
Textos: "texto"
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
print("Hola " + "Pelol") # concatenar texto
print("Hola ""Pelol") # concatenar texto

# Variables que guardan valores
hola = "Hola " # Ahora cada vez que escribimos hola, representa la cadena "Hola "
pelol = "Pelol" 

print(hola + pelol) # concatenar texto
print("Pelol estuvo aqui " * 5) # repetir texto
print("Pelol estuvo aqui " + str(5) + " " + "veces")

veinte = 20

print(str(veinte) + str(veinte)) # 2020
print("Las \"comillas dobles escapadas\" tambien sirven") # repetir texto
print('Las "comillas simples" tambien sirven') # repetir texto

print("""\

  Operaciones con texto
  En muchas lineas

""")

# Booleanos (operadores binarios) y variables
print("\nBooleanos (operadores binarios) y variables")

print(True) # verdadero
print(False) # falso
print(True and True) # verdadero y verdadero = verdadero
print(True or True) # verdadero o verdadero = verdadero
print(False and True) # falso y verdadero = falso
print(False or True) # falso o verdadero = verdadero
print(False and False) # falso y falso = falso
print(False or False) # falso o falso = falso
print(not True) # falso
print(not False) # verdadero

# 67 esta entre 20 y 90
print(67 > 20 and 67 < 90) # excluye 20 y 90
print(67 >= 20 and 67 <= 90) # incluye 20 y 90
print(67 > 20 and 67 <= 90) # incluye 90 y excluye 20
print(67 >= 20 and 67 < 90) # incluye 20 y excluye 90

# variables para simplificar y generar consistencia
sesenta_y_siete = 67
noventa = 90

print(sesenta_y_siete > veinte and sesenta_y_siete < noventa) # excluye 20 y 90
print(sesenta_y_siete >= veinte and sesenta_y_siete <= noventa) # incluye 20 y 90
print(sesenta_y_siete > veinte and sesenta_y_siete <= noventa) # incluye 90 y excluye 20
print(sesenta_y_siete >= veinte and sesenta_y_siete < noventa) # incluye 20 y excluye 90

dos_mayor_a_uno = 2 > 1
dos_menor_a_uno = 2 < 1
cuarenta_y_dos = 42

print(dos_mayor_a_uno)
print("Numero favorito: " + str(cuarenta_y_dos))
print("Numero favorito: {}".format(cuarenta_y_dos))
print(f"Numero favorito: {cuarenta_y_dos}")
print("2 > 1 es {}".format(dos_mayor_a_uno)) # formatear variables
print(dos_menor_a_uno)
print(f"2 < 1 es {dos_menor_a_uno}") # formatear variables de manera linda

# Ejemplos de Métodos
print("\nEjemplos de Métodos")
print("estoy gritando".upper())

grito = "eStoY GrItaNdo"

print(grito.swapcase())

print("Macri es un capo".replace("Macri", "Pelol"))
print("Macri es un capo".replace("capo", "gato".upper()))

# Listas
print("\nListas")
print([1, "dos", True])

# Las listas agrupan elementos en orden 0, 1, 2, 3,..., n - 1, siendo n la cantidad de elementos de la lista
# Las listas siempre están ordenadas
#        0  1  2  3         4

lista = [1, 2, 3, "cuatro", False]

print(f"\nLista inicial: {lista}")
print(f"Cantidad de elementos de la lista {len(lista)}")
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
print(len(cuatro)) # longitud del texto "cuatro", tiene 6 caracteres
print(list(cuatro)) # podes transformar texto en una lista

c = cuatro[0] # Podes sacar caracteres de un texto de la misma forma que elementos de una lista "c"
print(c)

# Diccionarios
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

usuarix1 = {
  "nombre": "Usuarix 1",
  "roles": ["DJ", "admin"]
}

usuarix2 = {
  "nombre": "Usuarix 2",
  "roles": ["DJ"]
}

usuarixs = [usuarix1, usuarix2]

# nombre de usuarix 1

adjetivo = diccionario["adjetivo"]
subelemento = diccionario["lenguajes de programacion"]["python"]

la_4_440 = { "tecla": 49, "frecuencia": 440 }

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
