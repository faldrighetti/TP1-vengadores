from diccionario import devolver_diccionario
import random


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
