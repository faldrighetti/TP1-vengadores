import diccionario
import ahorcado
import constantes as const


def seleccion_palabra(desea_letras):
    """
    Autor: Federico Aldrighetti.

    Esta función pregunta al usuario si quiere jugar con una cantidad determinada de letras. Si dice que sí,
    le pide que especifique la cantidad y le da la palabra con esa longitud validada. En caso contrario, le
    proporciona una palabra con una longitud al azar.
    """

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
        palabra_adivinar = seleccion_palabra(input(const.INTRODUZCA_COMANDO_DE_NUEVO))

    return palabra_adivinar


def jugar_una_partida():
    """
    Autor: Facundo Sanso.

    La función inicializa la partida
    """
    palabra_a_adivinar = seleccion_palabra(input(const.DESEA_LETRAS))
    return ahorcado.jugar_ahorcado(palabra_a_adivinar)


def jugar_multiples_partidas():
    """
    Autor: Facundo Sanso.

    Esta función aparece al finalizar una partida. Le da una opción al usuario de seguir jugando. En caso de
    decir que no, devuelve el puntaje final y un mensaje de despedida.
    En caso de que la respuesta sea positiva, el programa inicializará una partida nueva.
    """
    puntaje = jugar_una_partida()

    seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    while seguir_jugando.lower() == "si":
        puntaje += jugar_una_partida()
        seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    print(f"\nPuntaje total = {puntaje}")
    print(const.MENSAJE_DESPEDIDA)


jugar_multiples_partidas()
