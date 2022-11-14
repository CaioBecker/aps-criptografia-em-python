def criptografarTexto(cripto, texto):
    textoSeparado = []
    textoCriptografado = []

    count = 0
    while count < len(texto):
        textoSeparado.append(texto[count])
        count += 1

    for i in textoSeparado:
        textoCriptografado.append(cripto[i])

    texto = ''

    for i in textoCriptografado:
        texto = texto + str(i)

    return texto
