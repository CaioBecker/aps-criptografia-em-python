# CHAVES DA CIFRA DE CESAR

cifra_base = {'1': '1',
              '2': '2',
              '3': '3',
              '4': '4',
              '5': '5',
              '6': '6',
              '7': '7',
              '8': '8',
              '9': '9',
              '10': '0',
              '11': 'A',
              '12': 'B',
              '13': 'C',
              '14': 'D',
              '15': 'E',
              '16': 'F',
              '17': 'G',
              '18': 'H',
              '19': 'I',
              '20': 'J',
              '21': 'K',
              '22': 'L',
              '23': 'M',
              '24': 'N',
              '25': 'O',
              '26': 'P',
              '27': 'Q',
              '28': 'R',
              '29': 'S',
              '30': 'T',
              '31': 'U',
              '32': 'V',
              '33': 'W',
              '34': 'X',
              '35': 'Y',
              '36': 'Z',
              '37': 'a',
              '38': 'b',
              '39': 'c',
              '40': 'd',
              '41': 'e',
              '42': 'f',
              '43': 'g',
              '44': 'h',
              '45': 'i',
              '46': 'j',
              '47': 'k',
              '48': 'l',
              '49': 'm',
              '50': 'n',
              '51': 'o',
              '52': 'p',
              '53': 'q',
              '54': 'r',
              '55': 's',
              '56': 't',
              '57': 'u',
              '58': 'v',
              '59': 'w',
              '60': 'x',
              '61': 'y',
              '62': 'z',
              '63': ' ',
              '64': '!',
              '65': '@',
              '66': '#',
              '67': '$',
              '68': '%',
              '69': '^',
              '70': '&',
              '71': '*',
              '72': '(',
              '73': ')',
              '74': '-',
              '75': '_',
              '76': '=',
              '77': '+',
              '78': '[',
              '79': '{',
              '80': ']',
              '81': '}',
              '82': ';',
              '83': ':',
              '84': '|',
              '85': '<',
              '86': ',',
              '87': '>',
              '88': '.',
              '89': '?',
              '90': '°'}


def func_gerar_cifra(padrao):
    cifra_cesar = {}

    a = 1

    while a <= 90:
        index = 0
        if (a + padrao) > 90:
            index = (a + padrao) - 90
        else:
            index = a + padrao

        index = str(index)
        index_n = str(cifra_base[str(a)])
        cifra_cesar[index_n] = cifra_base[index]

        a = a + 1

    return cifra_cesar


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
    print(texto_cripto)
    for i in texto_cripto:
        texto = texto + str(i)

    return texto
