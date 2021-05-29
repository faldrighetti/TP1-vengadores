from diccionario import devolver_diccionario
import random

diccionario = devolver_diccionario()

def elegir_palabra(diccionario, cant_letras=0):
    lista = []
    condicion = False
    lista_de_palabras = list(diccionario.keys())
    while not str(cant_letras).isnumeric():
        cant_letras = input('Valor inválido, ingrese un número ')

    for palabra in lista_de_palabras:
        if len(palabra) == int(cant_letras):
            lista.append(palabra)
            condicion = True
    if condicion:
        palabra_adivinar = random.choice(lista)
    else:
        print(f'No encontramos una palabra de {cant_letras} letras, bancatela ')
        palabra_adivinar = random.choice(lista_de_palabras)
    return palabra_adivinar
