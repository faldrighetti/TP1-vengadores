archivo_cuentos = open('Cuentos.txt', 'r')
archivo_noches = open('Las 1000 Noches y 1 Noche.txt', 'r')
archivo_arania = open('La araña negra - tomo 1.txt', 'r')
archivo_palabras = open('palabras.csv', 'w')

lista_archivos = [archivo_cuentos, archivo_noches, archivo_arania]


def leer_info(archivo):

    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').replace('--', ' ').split()
    else:
        registro = False
    return registro


def creacion_de_listas(lista_archivos):

    (lista_palabras_cuentos, lista_palabras_noches, lista_palabras_arania) = ([], [], [])
    tupla_de_listas = (lista_palabras_cuentos, lista_palabras_noches, lista_palabras_arania)

    for archivo, lista_archivo in zip(lista_archivos, tupla_de_listas):
        contador_lineas_vacias = 0
        renglon = leer_info(archivo)
        while contador_lineas_vacias < 20:
            if not renglon:
                contador_lineas_vacias += 1
            else:
                contador_lineas_vacias = 0
                for palabra in renglon:
                    lista_archivo.append(palabra.lower())
            renglon = leer_info(archivo)

    return tupla_de_listas


def quitar_tildes(palabra):
    """
    Autor: Martin Morono.

    Devuelve la palabra ingresada eliminando la distinción entre letras sin tilde y letras con tilde.
    """
    cambios = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for vocal_con_tilde, vocal_sin_tilde in cambios:
        palabra = palabra.replace(vocal_con_tilde, vocal_sin_tilde).replace(
            vocal_con_tilde.upper(), vocal_sin_tilde.upper())
    return palabra


def limpiar_palabra(palabra):
    palabra_limpia = "".join(caracter.lower() if caracter.isalpha()
                             else "" for caracter in palabra)
    palabra_sin_tildes = quitar_tildes(palabra_limpia)
    return palabra_sin_tildes


def procesar_listas(tupla_de_listas):

    listas_procesadas = []
    for lista_palabras in tupla_de_listas:
        lista_palabras_procesada = []
        for palabra in lista_palabras:
            palabra = limpiar_palabra(palabra)
            if len(palabra) > 0:
                lista_palabras_procesada.append(palabra)
        listas_procesadas.append(lista_palabras_procesada)

    return ordenamiento_listas(listas_procesadas)


def ordenamiento_listas(tupla_de_listas):

    for lista_palabras in tupla_de_listas:
        lista_palabras.sort()

    return tupla_de_listas


def creacion_texto(lista_de_listas):

    indice_cuentos, indice_noches, indice_arania = (0, 0, 0)

    palabra_cuentos = lista_de_listas[0][indice_cuentos]
    palabra_noches = lista_de_listas[1][indice_noches]
    palabra_arania = lista_de_listas[2][indice_arania]

    # longitudes_listas = (len(lista_de_listas[0])-1,
    # len(lista_de_listas[1])-1, len(lista_de_listas[2])-1)

    # print(longitudes_listas)

    while indice_cuentos < (len(lista_de_listas[0])-1) and indice_noches < (len(lista_de_listas[1])-1) and indice_arania < (len(lista_de_listas[2])-1):

        palabra = min(palabra_cuentos, palabra_noches, palabra_arania)
        #print(indice_arania, (len(lista_de_listas[2])-1))
        contador_cuentos, contador_noches, contador_arania = (0, 0, 0)
        #print(palabra, palabra_cuentos, palabra_noches, palabra_arania)

        while palabra_cuentos == palabra:
            contador_cuentos += 1
            indice_cuentos += 1
            if indice_cuentos < len(lista_de_listas[0]):
                palabra_cuentos = lista_de_listas[0][indice_cuentos]

        while palabra_noches == palabra:
            contador_noches += 1
            indice_noches += 1
            if indice_noches < len(lista_de_listas[1]):
                palabra_noches = lista_de_listas[1][indice_noches]

        while palabra_arania == palabra:  # TRAUMADO
            contador_arania += 1
            indice_arania += 1
            if indice_arania < len(lista_de_listas[2]):
                palabra_arania = lista_de_listas[2][indice_arania]

        #print('ESCRIBE', palabra)
        archivo_palabras.write(
            f'{palabra},{contador_cuentos},{contador_noches},{contador_arania} \n')

    archivo_cuentos.close()
    archivo_noches.close()
    archivo_arania.close()
    archivo_palabras.close()


creacion_texto((procesar_listas(creacion_de_listas(lista_archivos))))
