from texto import obtener_texto
import constantes as const
import random


def quitar_tildes(palabra):
    cambios = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in cambios:
        palabra = palabra.replace(a, b).replace(a.upper(), b.upper())
    return palabra


def limpiar_palabra(palabra):
    palabra = "".join(caracter.lower() if caracter.isalpha() else "" for caracter in palabra)
    return quitar_tildes(palabra)


def obtener_dicc_palabras_candidatas():
    """
    TODO: Completar
    """
    texto_a_procesar = obtener_texto().replace("--", " ").split()

    dicc_palabras_validas = {}

    for palabra in texto_a_procesar:
        palabra = limpiar_palabra(palabra)
        if len(palabra) >= const.LONGITUD_MINIMA_PALABRA:
            if palabra in dicc_palabras_validas:
                dicc_palabras_validas[palabra] += 1
            else:
                dicc_palabras_validas[palabra] = 1

    return dicc_palabras_validas


def ordenar_diccionario(diccionario):
    lista_ordenada = sorted(diccionario.items(), key=lambda tupla: tupla[const.INDICE_CLAVE])
    return dict(lista_ordenada)


def devolver_diccionario():
    diccionario_palabras = obtener_dicc_palabras_candidatas()
    return ordenar_diccionario(diccionario_palabras)


def mostrar_diccionario():
    print(devolver_diccionario())
    print(f"\nEl diccionario contiene {len(devolver_diccionario().keys())} palabras")


def elegir_palabra(diccionario, cant_letras=0):
    """
    Devuelve una palabra aleatoria de la longitud elegida.
    - Si no se encuentra una palabra con la longitud ingresada devuelve None.
    - Si la longitud ingresada es 0, devuelve una palabra aleatoria de cualquier longitud.

    Parámetros:
    - diccionario: diccionario con las palabras a elegir.
    - cant_letras: longitud de la palabra a devolver.
    """

    lista_palabras = list(diccionario.keys());

    if cant_letras != 0:
        lista_palabras = list(filter(lambda palabra: len(palabra) == cant_letras, lista_palabras))

    return random.choice(lista_palabras) if lista_palabras else None


def test_elegir_palabra(diccionario):
    """
    Test de la función "elegir_palabra".
    Invoca a la función 10 veces con cada combinación de cant_letras (0 a 20).
    """
    
    for cant_letras in range(21):
        print(f"Palabras con {cant_letras} letras:")

        for _ in range(10):
            palabra = elegir_palabra(diccionario, cant_letras)
            if palabra:
                print(f"{palabra} - {len(palabra)}")
