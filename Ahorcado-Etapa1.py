palabra = 'termodinamica'

def convertir_palabra(palabra):   
    return (''.join('?' for i in range(len(palabra))))

letras_erroneas = []
letras_usadas = []
aciertos = 0
desaciertos = 0
aciertos_desaciertos = f'Aciertos: {aciertos}  Desaciertos: {desaciertos}, {letras_erroneas}'
palabra_descifrada = convertir_palabra(palabra)
mensaje = 'Palabra a adivinar'


while palabra_descifrada != palabra and desaciertos < 8: # bucle que se repite hasta que hayamos adivinado la palabra o hayamos tenido más de 7 errores
    print(f'{mensaje}: --> {palabra_descifrada}   {aciertos_desaciertos}')
    letra = input('Ingrese Letra: ') # cada vez que se repita el bucle, pedimos que se ingrese una letra
    if letra in ('0', 'FIN'):   # si se ingresa 0 o FIN, el juego termina
        break
    while letra in letras_usadas:   # verificamos que la letra no haya sido ingresada aún, si no, se pide una nueva letra
        letra = input('Letra ya ingresada, ingrese otra: ')
    while len(letra) != 1 or letra.isalpha() == False:  # verificamos que la letra sea, en efecto, una letra, y solo una
        letra = input('No ha ingresado una letra válida, ingrese 1 LETRA: ')
    if letra in palabra:    # subcódigo a ejecutar cuando la letra ingresada está en la letra por descifrar
        mensaje = 'Muy bien!!!'
        aciertos += 1
        lista_indices = []
        for indice in range(len(palabra)):  # hacemos una lista que contendrá los indices en donde se encuentra la letra ingresada en la palabra
            if palabra[indice] == letra:
                lista_indices.append(indice)
        lista_palabra_descifrada = list(palabra_descifrada)
        for indice in lista_indices:    #reemplazamos los ? por la letra en cuestión, debemos hacer una lista que contenga las letras y luego volver a formar el string a partir de dicha lista
            lista_palabra_descifrada[indice] = letra
            palabra_descifrada = ''.join(lista_palabra_descifrada)
    else:   # subcódigo a ejecutar cuando la letra ingresada no se encuentra en la palabra
        mensaje = 'Lo siento!!!'
        desaciertos += 1
        letras_erroneas.append(letra)
    letras_usadas.append(letra) # agregamos la letra ingresada a una lista que contiene todas las letras usadas
    print('') # imprime un enter para que el output sea más prolijo

    aciertos_desaciertos = f'Aciertos: {aciertos}  Desaciertos: {desaciertos}, {letras_erroneas}' # se utiliza para mostrar los aciertos y desaciertos en pantalla  tras cada letra ingresada

if palabra_descifrada == palabra: print(f'Ganaste! La palabra era {palabra}. ')
else: print('Lo siento! Has llegado a 8 desaciertos. ')
