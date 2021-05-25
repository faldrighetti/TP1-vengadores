from diccionario import devolver_diccionario
import random

diccionario = devolver_diccionario()

def elegir_palabra(diccionario,cant_letras=0):
    lista = []
    condicion = False
    lista_de_palabras = list(diccionario.keys())

    for palabra in lista_de_palabras:
        if len(palabra) == cant_letras:
            lista.append(palabra)
            condicion = True

    if condicion:
        palabra_adivinar = random.choice(lista)
    else:
        palabra_adivinar = random.choice(lista_de_palabras)

    return palabra_adivinar

print(elegir_palabra(diccionario,7))
