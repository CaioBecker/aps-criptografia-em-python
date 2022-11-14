from pickle import TRUE

import ChavesDeCriptografia as cdc
import AssociacaoFixaDeValores as afdv
import TransposicaoDeColunas as tdc

while TRUE:
    opcao = input('Criptografar-1 / Descriptografar-2\n')
    
    if opcao == '1' or opcao == '2':
        if opcao == '1':
            texto = input("Digite um texto para que seja criptografado: ")

            cripto1 = afdv.criptografarTexto(cdc.associacaoDeValores, texto)
            cripto2 = afdv.criptografarTexto(cdc.associacaoDeValores, cripto1)
            cripto3 = afdv.criptografarTexto(cdc.associacaoDeValores, cripto2)
            cripto4 = afdv.criptografarTexto(cdc.associacaoDeValores, cripto3)
            cripto5 = tdc.func_criptografar_coluna(cripto4, 'C')
            print(cripto1)
            print(cripto5)

        else:
            des_cripto_1 = tdc.func_criptografar_coluna(input("Digite um texto para descriptografar:\n"), 'D')
            des_cripto_2 = afdv.criptografarTexto(cdc.associacaoDeValoresVolta, des_cripto_1)
            des_cripto_3 = afdv.criptografarTexto(cdc.associacaoDeValoresVolta, des_cripto_2)
            des_cripto_4 = afdv.criptografarTexto(cdc.associacaoDeValoresVolta, des_cripto_3)
            des_cripto_5 = afdv.criptografarTexto(cdc.associacaoDeValoresVolta, des_cripto_4)
            print(f'Descriptografado: {des_cripto_5}')

        #VALOR PARA TESTE
        #1234567890abcdefghijklmnopqrstuvwxyz !@#$%^&*()-_=+[{]};:<,>.?
