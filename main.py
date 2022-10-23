import random
import chaves_cesar as cc

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



cripto_1 = func_criptografar(cc.cripto_cm_1, input("Digite um texto para criptografar:").upper())
print(cripto_1)
cripto_2 = func_criptografar(cc.cripto_cm_1, cripto_1)
print(cripto_2)
cripto_3 = func_criptografar(cc.cripto_cm_1, cripto_2)
print(cripto_3)
cripto_4 = func_criptografar(cc.cripto_cm_1, cripto_3)
print(cripto_4)
print('----------------')
cripto_volta_1 = func_criptografar(cc.cripto_cm_1_volta, cripto_4)
print(cripto_volta_1.upper())

#1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+[{]};:|<,>.?





