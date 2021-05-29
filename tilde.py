def quitar_tildes(palabra):
    cambios = (("á", "a"), ("é", "e"),("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in cambios:
        palabra = palabra.replace(a, b).replace(a.upper(), b.upper())
    return palabra
