from texto import obtener_texto
import constantes as const

# Devuelve una palabra únicamente con los caracteres (a-z) sin considerar números ni caracteres especiales

def quitar_tildes(palabra):
    cambios = (("á", "a"), ("é", "e"),("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in cambios:
        palabra = palabra.replace(a, b).replace(a.upper(), b.upper())
    return palabra

def limpiar_palabra(palabra):
    if '--' in palabra: palabra.replace('--',' ')
    palabra = "".join(caracter.lower() if caracter.isalpha() else "" for caracter in palabra)
    palabra_sin_tildes = quitar_tildes(palabra)
    return palabra_sin_tildes
# Devuelve el diccionario de palabras validas: sin repetidos, sin caracteres especiales, longitud valida.

def obtener_dic_palabras_candidatas():
    texto_a_procesar = obtener_texto().split() # se trae el texto y convierte toda la cadena en una lista donde cada
    # elemento va a ser una palabra y separa las palabras teniendo en cuenta los espacios.
    dicc_palabras_validas = {} # inicializo diccionario vacio

    # agrego las palabras al diccionario recorriendolas con el for
    for palabra in texto_a_procesar:
        palabra = limpiar_palabra(palabra) #recorremos las palabras de la lista quitando caracteres especiales
        if len(palabra) >= const.LONGITUD_MINIMA_PALABRA: #valido su longitud >= se incluye al diccionario
            if palabra in dicc_palabras_validas:
                dicc_palabras_validas[palabra] += 1 # si la palabra ya se encuentra en el diccionario (se la sumamos
                # con un contador)
            else:
                dicc_palabras_validas[palabra] = 1 # si la palabra no se encuentra en el dic, se inicializa en 1.

    return dicc_palabras_validas

# Convierte en lista para poder ordenar con algoritmo de ordenamiento.

def ordenar_diccionario(diccionario):
    lista_ordenada = sorted(diccionario.items(), key=lambda tupla: tupla[const.INDICE_CLAVE]) #items convierte de
    # diccionario a lista de tuplas
    #lambda indica bajo que criterio vamos a ordenar (por keys(posicion 0)
    diccionario_ordenado = dict(lista_ordenada)
    return diccionario_ordenado

def devolver_diccionario():
    diccionario_palabras = obtener_dic_palabras_candidatas()
    return ordenar_diccionario(diccionario_palabras)

def mostrar_diccionario():
    diccionario_palabras = obtener_dic_palabras_candidatas()
    print(devolver_diccionario())
    print(f"\nEl diccionario contiene {len(diccionario_palabras.keys())} palabras")
