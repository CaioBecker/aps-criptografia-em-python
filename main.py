def func_criptografar():



cripto = {'1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 0, '0': 1}

texto_quebrado = []

texto_cripto = []

texto = input("Digite um texto para criptografar:")
count = 0
while count < len(texto):
    texto_quebrado.append(texto[a])
    count = count + 1


for i in texto_quebrado:
    print(i)
    texto_cripto.append(cripto[i])

print(texto)
texto = ''

for i in texto_cripto:
    texto = texto + str(i)

print(texto)
