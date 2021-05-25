import constantes as const
from etapa3 import elegir_palabra
from diccionario import devolver_diccionario

diccionario = devolver_diccionario()

def ofuscar_palabra(palabra, letras_adivinadas):
    return "".join(letra if letra in letras_adivinadas else const.SIGNO_PREGUNTA for letra in palabra)

def mostrar_informacion(mensaje, palabra, letras_adivinadas, letras_erroneas):
    palabra = ofuscar_palabra(palabra, letras_adivinadas)
    print(f"\n{mensaje} → {palabra}  Aciertos: {len(letras_adivinadas)}  Desaciertos: {len(letras_erroneas)} - {letras_erroneas}")

def pedir_letra(letras_usadas):
    letra_valida = False
    letra = ""

    while not letra_valida and letra not in const.LETRAS_FIN:
        letra = input(const.MENSAJE_INPUT_LETRA)

        if len(letra) != 1 or not letra.isalpha():
            print(f"\n{const.MENSAJE_INGRESO_INVALIDO}")
        elif letra in letras_usadas:
            print(f"\n{const.MENSAJE_LETRA_INGRESADA}")
        else:
            letra_valida = True

    return letra

def seleccion_palabra(desea_letras):
    if desea_letras == 'si':
        cuantas_letras = input('Cuantas letras? ')
        palabra_adivinar = elegir_palabra(diccionario, cuantas_letras)
    else:
        palabra_adivinar = elegir_palabra(diccionario)

    return palabra_adivinar

def continuar_jugando(SEGUIR_JUGANDO):
    if SEGUIR_JUGANDO == "si" :
        jugar_ahorcado(seleccion_palabra(input('Desea una cantidad de letras específica? (si/no) ')))
    else:
        print("Gracias por jugar!!!")
        print("Tu puntaje fue:", const.PUNTAJE_DEL_JUEGO)

def jugar_ahorcado(palabra):
    letra = ""
    letras_adivinadas = []
    letras_erroneas = []
    gano = False

    mostrar_informacion(const.MENSAJE_INICIAL, palabra, letras_adivinadas, letras_erroneas)

    while letra not in const.LETRAS_FIN and len(letras_erroneas) < 7 and not gano:
        letra = pedir_letra(letras_adivinadas + letras_erroneas)

        if letra in palabra:
            letras_adivinadas.append(letra)
            mensaje = const.MENSAJE_ACIERTO
            const.PUNTAJE_DEL_JUEGO += 10
        else:
            letras_erroneas.append(letra)
            mensaje = const.MENSAJE_DESACIERTO
            const.PUNTAJE_DEL_JUEGO -= 5

        mostrar_informacion(mensaje, palabra, letras_adivinadas, letras_erroneas)
        gano = len(set(palabra)) == len(letras_adivinadas)


    return f"¡Ganaste!", continuar_jugando(input(const.SEGUIR_JUGANDO)) if gano else print("Perdiste :(", const.PUNTAJE_DEL_JUEGO)



jugar_ahorcado(seleccion_palabra(input('Desea una cantidad de letras específica? (si/no) ')))
