from diccionario import devolver_diccionario
import random

diccionario = devolver_diccionario()

def elegir_palabra(diccionario,cant_letras=0):
    lista = []
    lista_de_palabras = list(diccionario.keys())
    lista_longitudes = []
    lista_longitudes = [len(palabra) for palabra in lista_de_palabras if len(palabra) not in lista_longitudes]
    while not str(cant_letras).isnumeric():
        cant_letras = input('Valor inválido, ingrese un número ')
    if cant_letras in lista_longitudes:
        for palabra in lista_de_palabras:
            if len(palabra) == int(cant_letras):
                lista.append(palabra)
    else:
        if int(cant_letras) > max(lista_longitudes):
            for palabra in lista_de_palabras:
                if len(palabra) == max(lista_longitudes):
                    lista.append(palabra)
        if int(cant_letras) < min(lista_longitudes):
            for palabra in lista_de_palabras:
                if len(palabra) == min(lista_longitudes):
                    lista.append(palabra)

    palabra_adivinar = random.choice(lista)

    return palabra_adivinar

print(elegir_palabra(diccionario, 'dfkd'))
