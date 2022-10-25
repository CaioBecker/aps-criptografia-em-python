def CriptografarPorColunas(cripto_4):
    texto_separado = []
    text_criptografado_pronto = []
    texto_criptografado = {}

    a = 0
    while a < len(cripto_4):
        texto_separado.append(cripto_4[a])
        a += 1

    b = 0
    control = len(texto_separado) - 3
    while b <= control:
        texto_criptografado[str(texto_separado[0:3])] = b
        del (texto_separado[0:3])
        b += 1

    for teste in texto_criptografado.keys():
        if teste == "[]":
            del (texto_criptografado[teste])

    print(texto_criptografado)

    """text_criptografado_pronto.append(texto_criptografado)
    texto_separado = []
    for texto in text_criptografado_pronto:
        for x, y in texto.items():
            texto_separado.append(x + ": " + str(y))
    """
    print(texto_separado)
    print(control)
