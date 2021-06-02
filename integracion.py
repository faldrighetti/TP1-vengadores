import diccionario
import ahorcado
import constantes as const


def seleccion_palabra(desea_letras):
    dicc = diccionario.devolver_diccionario()

    if desea_letras.lower() == 'si':
        cant_letras = input('Cuantas letras? ')
        while not cant_letras.isnumeric() or diccionario.elegir_palabra(dicc, int(cant_letras)) == None:
            if not cant_letras.isnumeric():
                cant_letras = input('Ingrese cantidad de letras correcta: ')
            elif diccionario.elegir_palabra(dicc, int(cant_letras)) == None:
                cant_letras = input(
                    f'No hay palabras con esa longitud. Elige una longitud entre {const.LONGITUD_MINIMA_PALABRA} y {const.LONGITUD_MAXIMA_PALABRA}: ')

        palabra_adivinar = diccionario.elegir_palabra(dicc, int(cant_letras))

    elif desea_letras.lower() == 'no':
        palabra_adivinar = diccionario.elegir_palabra(dicc)

    else:
        palabra_adivinar = seleccion_palabra(input('Introduzca si o no: '))

    return palabra_adivinar


def continuar_jugando(SEGUIR_JUGANDO):  # sacar mas adelante
    if seguir_jugando == "si":
        jugar_ahorcado(seleccion_palabra(input(const.DESEA_LETRAS)))
    elif seguir_jugando == "no":
        print("Gracias por jugar!!!")
        print("Tu puntaje fue:", const.PUNTAJE_DEL_JUEGO)
    else:
        print(continuar_jugando(input(const.INTRUZCA_COMANDO_DE_NUEVO)))


def jugar_una_partida():
    palabra_a_adivinar = seleccion_palabra(input(const.DESEA_LETRAS))
    return ahorcado.jugar_ahorcado(palabra_a_adivinar)


def jugar_multiples_partidas():
    puntaje = jugar_una_partida()

    seguir_jugando = input(const.SEGUIR_JUGANDO)

    while seguir_jugando.lower() == "si":
        puntaje += jugar_una_partida()
        seguir_jugando = input(const.SEGUIR_JUGANDO)

    print(f"Puntaje total = {puntaje}")
    print("Gracias por jugar!!!")


jugar_multiples_partidas()  # TODO: No funciona, revisar!
