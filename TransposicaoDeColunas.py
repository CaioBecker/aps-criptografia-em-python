def func_criptografar_coluna(cripto,tp):
    texto_separado = []
    text_criptografado_pronto = ''
    dc_arrays = {1: [], 2: [], 3: [], 4: []}

    #COLOCAR TRY

    a = 0
    while a < len(cripto):
        texto_separado.append(cripto[a])
        a += 1

    a = 0

    while a < round(len(cripto)/3):
        dc_arrays[1].append(texto_separado[0])
        del (texto_separado[0])
        dc_arrays[2].append(texto_separado[0])
        del (texto_separado[0])
        dc_arrays[3].append(texto_separado[0])
        del (texto_separado[0])

        a += 1

    if tp == 'D' :
        dc_arrays[4] = dc_arrays[2]
        dc_arrays[2] = dc_arrays[1]
        dc_arrays[1] = dc_arrays[3]
        dc_arrays[3] = dc_arrays[4]
    else:
        dc_arrays[4] = dc_arrays[1]
        dc_arrays[1] = dc_arrays[2]
        dc_arrays[2] = dc_arrays[3]
        dc_arrays[3] = dc_arrays[4]

    a = 0

    while a < round(len(cripto) / 3):

        text_criptografado_pronto = text_criptografado_pronto + dc_arrays[1][a]
        text_criptografado_pronto = text_criptografado_pronto + dc_arrays[2][a]
        text_criptografado_pronto = text_criptografado_pronto + dc_arrays[3][a]

        a += 1


    return text_criptografado_pronto
    #for i in dc_arrays[1]:
    #    print(i)
