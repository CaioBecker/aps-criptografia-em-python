import random
import chaves_cesar as cc
import TransposicaoDeColunas as tdc

def func_criptografar(cripto, texto):
    texto_quebrado = []
    texto_cripto = []

    count = 0
    while count < len(texto):
        texto_quebrado.append(texto[count])
        count = count + 1

    for i in texto_quebrado:
        r = random.randint(1, 3)
        if r == 1:
            texto_cripto.append(cripto[i.upper()].lower())
        else:
            texto_cripto.append(cripto[i.upper()].upper())

    texto = ''
    for i in texto_cripto:
        texto = texto + str(i)

    return texto

cripto_1 = func_criptografar(cc.cripto_cc, input("Digite um texto para criptografar:\n").upper())
cripto_2 = func_criptografar(cc.cripto_cc, cripto_1)
cripto_3 = func_criptografar(cc.cripto_cc, cripto_2)
cripto_4 = func_criptografar(cc.cripto_cc, cripto_3)
print(f'Cifra de cesar:{cripto_4}')

cripto_5 = tdc.func_criptografar_coluna(cripto_4, 'C')

print(f'Tranpocicao de colunas:{cripto_5}')

des_cripto_1 = tdc.func_criptografar_coluna(cripto_5, 'D')

des_cripto_2 = func_criptografar(cc.cripto_cc_volta, des_cripto_1)

print(f'Descriptografado:{des_cripto_2.upper()}')

#VALOR PARA TESTE
#1234567890abcdefghijklmnopqrstuvwxyz !@#$%^&*()-_=+[{]};:|<,>.?
