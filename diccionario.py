from texto import obtener_texto
import constantes as const


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


mostrar_diccionario()