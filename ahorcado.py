import constantes as const


def ofuscar_palabra(palabra, letras_adivinadas):
    """
    Ofusca las letras de la palabra que todavía no han sido adivinadas utilizando signos de pregunta (?)

    Parámetros:
    - palabra: palabra a ofuscar
    - letras_adivinadas: letras que no deben ofuscarse
    """

    return "".join(letra if letra in letras_adivinadas else const.SIGNO_PREGUNTA for letra in palabra)


def mostrar_informacion(mensaje, palabra, letras_adivinadas, letras_erroneas):
    """
    TODO: Completar
    """

    palabra = ofuscar_palabra(palabra, letras_adivinadas)
    print(f"\n{mensaje} → {palabra}  Aciertos: {len(letras_adivinadas)}  Desaciertos: {len(letras_erroneas)} - {letras_erroneas}")


def pedir_letra(letras_usadas):
    """
    Solicita una letra al usuario realizando las siguientes validaciones:
    - Se ingresó un único caracter válido (no numérico o especial)
    - La letra no se utilizó en intentos anteriores
    - La letra no es un caracter utilizado para finalizar el juego.

    Devuelve la letra ingresada por el usuario en minúscula.

    Parámetros:
    - letras_usadas: Lista de letras ya utilizadas
    """

    letra_valida = False
    letra = ""

    while not letra_valida and letra not in const.LETRAS_FIN:
        letra = input(const.MENSAJE_INPUT_LETRA)
        letra = letra.lower()

        if len(letra) != 1 or not letra.isalpha():
            print(f"\n{const.MENSAJE_INGRESO_INVALIDO}")

        elif letra in letras_usadas:
            print(f"\n{const.MENSAJE_LETRA_INGRESADA}")

        else:
            letra_valida = True

    return letra


def tiene_intentos(letras_erroneas):
    """
    Devuelve True si el usuario cuenta con intentos disponibles, es decir,
    si la cantidad de letras erróneas ingresadas es menor a la cantidad máxima de desaciertos permitidos.
    """
    return len(letras_erroneas) < const.MAXIMOS_DESACIERTOS_PERMITIDOS


def finalizar_juego(letra):
    """
    Devuelve True si la letra ingresada por el usuario es una letra de fin utilizada para finalizar el juego.
    """
    return letra in const.LETRAS_FIN


def juego_ganado(palabra, letras_adivinadas):
    """
    Devuelve True si el jugador adivinó todas las letras de la palabra.
    """
    return len(set(palabra)) == len(letras_adivinadas)


def mostrar_mensaje_final(palabra, letras_adivinadas, letra):
    """
    TODO: Completar
    """
    mensaje = ""

    if juego_ganado(palabra, letras_adivinadas):
        mensaje = "¡Ganaste!"

    elif letra in const.LETRAS_FIN:
        mensaje = "Gracias por participar"
    
    else:
        mensaje = f"Perdiste :(, la palabra era: {palabra}"
    
    print(mensaje)


def jugar_ahorcado(palabra):
    """
    TODO: Completar
    """

    letra = ""
    letras_adivinadas = []
    letras_erroneas = []
    puntaje = 0

    mostrar_informacion(const.MENSAJE_INICIAL, palabra,letras_adivinadas, letras_erroneas)

    while not finalizar_juego(letra) and tiene_intentos(letras_erroneas) and not juego_ganado(palabra, letras_adivinadas):
        letra = pedir_letra(letras_adivinadas + letras_erroneas)

        if letra in palabra:
            letras_adivinadas.append(letra)
            mensaje = const.MENSAJE_ACIERTO
            puntaje += const.PUNTAJE_ACIERTO

        else:
            letras_erroneas.append(letra)
            mensaje = const.MENSAJE_DESACIERTO
            puntaje += const.PUNTAJE_DESACIERTO

        mostrar_informacion(mensaje, palabra, letras_adivinadas, letras_erroneas)
    
    mostrar_mensaje_final(palabra, letras_adivinadas, letra)

    return puntaje
