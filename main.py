def func_criptografar(cripto, texto):
    texto_quebrado = []

    texto_cripto = []

    count = 0
    while count < len(texto):
        texto_quebrado.append(texto[count])
        count = count + 1

    for i in texto_quebrado:
        texto_cripto.append(cripto[i])

    texto = ''

    for i in texto_cripto:
        texto = texto + str(i)

    return texto

cripto_cm_1 = {'1': 'W',
               '2': 'X',
               '3': 'Y',
               '4': 'Z',
               '5': '!',
               '6': '@',
               '7': '#',
               '8': '$',
               '9': '%',
               '0': '^',
               'A': '&',
               'B': '*',
               'C': '(',
               'D': ')',
               'E': '-',
               'F': '_',
               'G': '=',
               'H': '+',
               'I': '[',
               'J': '{',
               'K': ']',
               'L': '}',
               'M': ';',
               'N': ':',
               'O': '|',
               'P': '<',
               'Q': ',',
               'R': '>',
               'S': '.',
               'T': '?',
               'U': '1',
               'V': '2',
               'W': '3',
               'X': '4',
               'Y': '5',
               'Z': '6',
               '!': '7',
               '@': '8',
               '#': '9',
               '$': '0',
               '%': 'A',
               '^': 'B',
               '&': 'C',
               '*': 'D',
               '(': 'E',
               ')': 'F',
               '-': 'G',
               '_': 'H',
               '=': 'I',
               '+': 'J',
               '[': 'K',
               '{': 'L',
               ']': 'M',
               '}': 'N',
               ';': 'O',
               ':': 'P',
               '|': 'Q',
               '<': 'R',
               ',': 'S',
               '>': 'T',
               '.': 'U',
               '?': 'V'}

cripto_cm_1_volta = {'1': ',',
                     '2': '>',
                     '3': '.',
                     '4': '?',
                     '5': '1',
                     '6': '2',
                     '7': '3',
                     '8': '4',
                     '9': '5',
                     '0': '6',
                     'A': '7',
                     'B': '8',
                     'C': '9',
                     'D': '0',
                     'E': 'A',
                     'F': 'B',
                     'G': 'C',
                     'H': 'D',
                     'I': 'E',
                     'J': 'F',
                     'K': 'G',
                     'L': 'H',
                     'M': 'I',
                     'N': 'J',
                     'O': 'K',
                     'P': 'L',
                     'Q': 'M',
                     'R': 'N',
                     'S': 'O',
                     'T': 'P',
                     'U': 'Q',
                     'V': 'R',
                     'W': 'S',
                     'X': 'T',
                     'Y': 'U',
                     'Z': 'V',
                     '!': 'W',
                     '@': 'X',
                     '#': 'Y',
                     '$': 'Z',
                     '%': '!',
                     '^': '@',
                     '&': '#',
                     '*': '$',
                     '(': '%',
                     ')': '^',
                     '-': '&',
                     '_': '*',
                     '=': '(',
                     '+': ')',
                     '[': '-',
                     '{': '_',
                     ']': '=',
                     '}': '+',
                     ';': '[',
                     ':': '{',
                     '|': ']',
                     '<': '}',
                     ',': ';',
                     '>': ':',
                     '.': '|',
                     '?': '<'


                     }

cripto_1 = func_criptografar(cripto_cm_1, input("Digite um texto para criptografar:").upper())
print(cripto_1)
cripto_2 = func_criptografar(cripto_cm_1, cripto_1)
print(cripto_2)
cripto_3 = func_criptografar(cripto_cm_1, cripto_2)
print(cripto_3)
cripto_4 = func_criptografar(cripto_cm_1, cripto_3)
print(cripto_4)
print('----------------')
cripto_volta_1 = func_criptografar(cripto_cm_1_volta, cripto_4)
print(cripto_volta_1)

#1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+[{]};:|<,>.?





