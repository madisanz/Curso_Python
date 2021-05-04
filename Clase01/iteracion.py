cadena = "Ejemplo con for"

number_of_characters = 0

for c in cadena:
    if c.lower() == "o":
        number_of_characters += 1

print("El numero de 'o' es:", number_of_characters)