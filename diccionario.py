from texto import obtener_texto
import constantes as const

# Devuelve una palabra únicamente con los caracteres (a-z) sin considerar números ni caracteres especiales
def limpiar_palabra(palabra):
    return "".join(caracter if caracter.isalpha() else "" for caracter in palabra)

# Devuelve el diccionario de palabras validas: sin repetidos, sin caracteres especiales, longitud valida.
#TODO: Arreglar bug de caracteres especiales (revisar split)
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
#TODO:ordenamiento de palabras que comienzan con tilde
def ordenar_diccionario(diccionario):
    lista_ordenada = sorted(diccionario.items(), key=lambda tupla: tupla[const.INDICE_CLAVE]) #items convierte de
    # diccionario a lista de tuplas
    #lambda indica bajo que criterio vamos a ordenar (por keys(posicion 0)
    diccionario_ordenado = dict(lista_ordenada)
    return diccionario_ordenado

# Mostrar el diccionario
def mostrar_diccionario():
    diccionario_palabras = obtener_dic_palabras_candidatas()
    print(ordenar_diccionario(diccionario_palabras))
    print(f"\nEl diccionario contiene {len(diccionario_palabras.keys())} palabras")

mostrar_diccionario()
