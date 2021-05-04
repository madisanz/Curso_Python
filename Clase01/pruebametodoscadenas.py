'''
#upper() para poner todo en mayusculas

name = input('Ingrese su nombre de usuario: ')
print('El nombre es: ', name.upper())



# lower() si pongo el nombre en mayusculas me lo devuelve en minisculas
name = input('Ingrese su nombre de usuario: ')
print('El nombre es: ', name.lower())


# capitalize() primera letra en Mayusculas
name = input('Ingrese su nombre de usuario: ')
print('El nombre es: ', name.capitalize())

upper() sube todo en mayúsculas
lower() baja todo en minúscula
capitalize() todas la primera letra en mayúscula
count() contar una y cuantas aparecen dentro de una cadena
find() representa el índice donde aparece un carácter dentro de un texto
isdigit() devuelve un booleano si es un valor numérico o no
isalum() comprueba si es alfanuméricos
isalpha si es alpha comprueba si son solo letras
split()  separa por palabras utilizando espacios
strip() borra los espacios sobrante al principio y al final
replace() cambia una palabra o una letra por otra
rfind() representa el índice de un carácter contando desde


s.endswith(suffix)     # Verifica si termina con el sufijo
s.find(t)              # Primera aparición de t en s (o -1 si no está)
s.index(t)             # Primera aparición de t en s (error si no está)
s.isalpha()            # Verifica si los caracteres son alfabéticos
s.isdigit()            # Verifica si los caracteres son numéricos
s.islower()            # Verifica si los caracteres son minúsculas
s.isupper()            # Verifica si los caracteres son mayúsculas
s.join(slist)          # Une una lista de cadenas usando s como delimitador
s.lower()              # Convertir a minúsculas
s.replace(old,new)     # Reemplaza texto
s.split([delim])       # Parte la cadena en subcadenas
s.startswith(prefix)   # Verifica si comienza con un sufijo
s.strip()              # Elimina espacios en blanco al inicio o al final
s.upper()              # Convierte a mayúsculas


#isdigit()  el método me devuelve False si hago un string o un True si son numeros 
edad = input('Introduce la edad: ')

print(edad.isdigit())

nombre = 'Naranja'
cajones = 100
precio = 91.1
a = f'{nombre:>10s} {cajones:10d} {precio:10.2f}'
print(a)


letrao = 'o'
contador = 0

if letrao in cadena:
    cadena = "Ejemplo con for"
    for letrao in cadena:
        print('caracter:', c)
        contador =+ 1
'''
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

frutas0 = frutas.lower()

print(frutas0)

frutas.find('Mandarina')