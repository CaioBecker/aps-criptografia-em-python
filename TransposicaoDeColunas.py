def CriptografarPorColunas(cripto_4):
    texto_separado = []
    texto_criptografado = {}

    count = 0
    while count < len(cripto_4):
        texto_separado.append(cripto_4[count])
        count += 1

    i = 0
    while i <= len(texto_separado):
        teste = str(texto_separado[0:3])
        texto_criptografado[teste] = i
        del (texto_separado[0:3])
        i += 1

    print(texto_criptografado)
