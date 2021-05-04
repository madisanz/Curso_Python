palabras = 'todos somos programadores'

frase_t = ""

for palabra in palabras:
    ultimo_segmento = palabra[-2:]
    
    if "a" in ultimo_segmento:
        ultimo_segmento = ultimo_segmento.replace("a", "e")
        palabra = palabra.replace(palabra[-2:], ultimo_segmento)
    if "o" in ultimo_segmento:
        ultimo_segmento = ultimo_segmento.replace("o", "e")
        palabra = palabra.replace(palabra[-2:], ultimo_segmento)
    
    frase_t += palabra + " "

print(frase_t)