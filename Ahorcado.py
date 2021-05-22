import Constantes as const

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
        else:
            letras_erroneas.append(letra)
            mensaje = const.MENSAJE_DESACIERTO

        mostrar_informacion(mensaje, palabra, letras_adivinadas, letras_erroneas)
        gano = len(set(palabra)) == len(letras_adivinadas)

    print(f"¡Ganaste!") if gano else print("Perdiste :(")

jugar_ahorcado("vengadores")