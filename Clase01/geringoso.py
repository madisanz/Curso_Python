# geringoso.py


# Ejercicio 1.18

# 
# >>> cadena = 'Geringoso'
# >>> capadepenapa = ''
# >>> for c in cadena:
#         ?
# >>> capadepenapa
# Geperipingoposopo


cadena = "geringoso"
capadepenapa = ""

vocales = "aeiou"

for c in cadena:
    if c in vocales:
        capadepenapa += c + "p" + c 
    else:
        capadepenapa += c

print(capadepenapa)

# Output

# python geringoso.py 
# Geperipingoposopo

