import random

def criptografarTexto(cripto, texto):
    textoSeparado = []
    textoCriptografado = []

    count = 0
    while count < len(texto):
        textoSeparado.append(texto[count])
        count += 1

    for i in textoSeparado:
        r = random.randint(1, 3)
        if r == 1:
            textoCriptografado.append(cripto[i.upper()].lower())
        else:
            textoCriptografado.append(cripto[i.upper()].upper())

    texto = ''

    for i in textoCriptografado:
        texto = texto + str(i)

    return texto
