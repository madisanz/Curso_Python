# Margarita Sánchez
# madisanz1@gmail.com

# solucion_de_errores.py

from pprint import pprint
import csv


def tiene_a(expresion):
   n = len(expresion)
   i = 0
   while i < n:
       if expresion[i] == 'a':
           print(f'Detecto {expresion[i]}')  # Para testear
           return True
       else:
           print('No')  # Para testear
           # return False # Lo comento para que no salga del while al leer el primer char
       i += 1


tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


def tiene_a(expresion):
   n = len(expresion)
   i = 0
   while i < n:
       if expresion[i] == 'a':
           # print('Si detecta') # Para testear
           return True
       i += 1
   return False


def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
            print(tiene)
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')


def suma(a, b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")

# Ejercicio 3.5: Pisando memoria
# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion("Data/camion.csv")
# pprint(camion)

# El problema aca es que se pisan los valores de una fila con la anterior. Esto se debe a que
# se le da un valor a cada registro[encabezado[n]], que en este caso son los valores de la
# ultima fila del archivo.

# Codigo corregido:


def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(
                zip(encabezado, (fila[0], int(fila[1]), float(fila[2]))))
            camion.append(registro)
    return camion


camion = leer_camion("Data/camion.csv")
pprint(camion
