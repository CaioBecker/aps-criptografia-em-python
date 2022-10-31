from pickle import TRUE

import chaves_cesar as cc
import TransposicaoDeColunas as tdc

while TRUE:
    opcao = input('Criptografar-1 / Descriptografar-2\n')
    
    if opcao == '1' or opcao == '2':
        if opcao == '1':
            
            padrao = int(input("Digite o padrão para a cifra de cesar:\n"))
            
            cifra = cc.func_gerar_cifra(padrao, 'C')
            
            cripto_1 = cc.func_criptografar(cifra, input("Digite um texto para criptografar:\n"))
            padrao = padrao + padrao
            print(padrao)
            """cripto_2 = cc.func_criptografar(cifra, cripto_1)
            padrao = padrao + padrao
            print(padrao)
            cripto_3 = cc.func_criptografar(cifra, cripto_2)
            padrao = padrao + padrao
            print(padrao)
            cripto_4 = cc.func_criptografar(cifra, cripto_3)
            padrao = padrao + padrao
            print(padrao)"""
            print(cifra)
            print(f'Cifra de cesar: "{cripto_1}"')

            cripto_5 = tdc.func_criptografar_coluna(cripto_1, 'C')

            print(f'Tranpocicao de colunas: "{cripto_5}"')
        else:
            
            padrao = int(input("Digite o padrão para a cifra de cesar:\n"))

            cifra = cc.func_gerar_cifra(padrao, 'D')

            cifra_des = cc.func_gerar_cifra_descripto(cifra)

            print(cifra_des)

            des_cripto_1 = tdc.func_criptografar_coluna(input("Digite um texto para descriptografar:\n"), 'D')
            des_cripto_2 = cc.func_criptografar(cifra_des, des_cripto_1)

            print(f'Descriptografado: {des_cripto_2}')

        #VALOR PARA TESTE
        #1234567890abcdefghijklmnopqrstuvwxyz !@#$%^&*()-_=+[{]};:|<,>.?
