"""Repaso de Python"""
# Comentario de una linea
"""
Comentario de varias lineas
"""
"""
Tipos de Datos
    - numericos: int, float
    - texto: str
    - booleanos: bool
    - listas: list
    - tuplas: tuple
    - diccionarios: dict
    - conjuntos: set
"""

""" Datos Numericos"""
num = 1 # int
num2 = 1.5 # float

"""
Calculo matematico de un int + float = float
"""
num = 1
num2 = 2
resultado = num + num2
resultado = 3

""" Datos de Texto"""
mensaje = "hola mundo"
mensaje2 = 'hola mundo'
mensaje3 = f'hola mundo'
saludo = "hola"
mensaje3 = f'{saludo} mundo' # hola mundo
mensaje4 = "hola" + " " + "mundo" # hola mundo

""" Datos Booleanos"""
verdadero = True
falso = False

""" Listas"""
lista = [1,2,3,4,5] # Cargamos la lista de con 5 elementos de forma manual
print(lista[2])
# lo podemos hacer con el input solictando la informacion al usuario
# lo podmeos cargar con un bucle

# cargar una lista con 10 elementos de forma dinamica
lista_elementos = []
for i in range(5):
    elemento = i + 1
    lista_elementos.append(elemento)
print(type(lista_elementos))
print(len(lista_elementos))
# Sumar las valores de la lista y dividirlo entre la cantidad
suma = sum(lista_elementos)
promedio = suma/ len(lista_elementos)
# print(type(promedio))

# ejemplo de un diccionario
mensaje = {
    "saludo": "hola",
    "despedida": "adios",
    "pregunta": "como estas?"
}
# print(mensaje["saludo"] + " " + mensaje["pregunta"] + " " + mensaje["despedida"])

# ejemplo de 2 numeros sumados que me den un resulado de 10
num1 = 100
num2 = -90
resultado = num1 + num2
# print(resultado)

#num1 = input("Ingrese el primer numero: ")# str
#num2 = input("Ingrese el segundo numero: ") # str
#resultado = int(num1) + int(num2) # Convertimos los string a int

# if resultado == 10:
#     print("Los valores ingresados suman 10")
# elif resultado != 10:
#     print("Los valores ingresados no suman 10")

# uso del While para solicitarle al usuario que ingrese 2 numeros que sumen 10
# while True:
#     num_1 = input("Ingrese el primer numero: ")# str
#     num_2 = input("Ingrese el segundo numero: ") # str
#     resultado = int(num_1) + int(num_2) # Convertimos los string a int

#     if resultado == 10:
#         print("Los valores ingresados suman 10")
#         break
#     elif resultado != 10:
#         print("Los valores ingresados no suman 10, intente nuevamente")

# funcion random
import random
numero_aleatorio = random.randint(1, 100)



def sumar():
    return 3 + 5

num_resultado = sumar()
print(num_resultado)
valor_total = num_resultado + 10
print(valor_total)







