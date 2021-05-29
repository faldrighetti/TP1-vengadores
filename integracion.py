import diccionario
import ahorcado
import constantes as const


def seleccion_palabra(desea_letras):
    dicc = diccionario.devolver_diccionario()

    if desea_letras.lower() == 's':
        cant_letras = input('Cuantas letras? ')
        while not cant_letras.isnumeric():
            cant_letras = input('Ingrese cantidad de letras correcta: ')
            
        palabra_adivinar = diccionario.elegir_palabra(dicc, cant_letras)
    
    else:
        palabra_adivinar = diccionario.elegir_palabra(dicc)

    return palabra_adivinar


def continuar_jugando(SEGUIR_JUGANDO):
    if SEGUIR_JUGANDO == "si":
        jugar_ahorcado(seleccion_palabra(input('Desea una cantidad de letras específica? (si/no) ')))
    elif SEGUIR_JUGANDO == "no":
        print("Gracias por jugar!!!")
        print("Tu puntaje fue:", const.PUNTAJE_DEL_JUEGO)
    else:
        print(continuar_jugando(input(const.INTRUZCA_COMANDO_DE_NUEVO)))


def jugar_una_partida():
    palabra_a_adivinar = seleccion_palabra(input('¿Desea una cantidad de letras específica? (s/n): '))
    return ahorcado.jugar_ahorcado(palabra_a_adivinar)


def jugar_multiples_partidas():
    puntaje = jugar_una_partida()

    seguir_jugando = input("Desea seguir jugando?: ")

    while seguir_jugando.lower() == "s":
        puntaje += jugar_una_partida()
        seguir_jugando = input("Desea seguir jugando?: ")
    
    print(f"Puntaje total = {puntaje}")


jugar_multiples_partidas() # TODO: No funciona, revisar!