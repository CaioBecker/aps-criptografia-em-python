import ChavesDeCriptografia as cdc
import AssociacaoFixaDeValores as afdv
import TransposicaoDeColunas as tdc

def criptografar():
    texto = input("Digite um texto para que possa ser Criptografado: ")

    cripto = afdv.criptografarTexto(cdc.associacaoDeValores, texto)
    ctrl = 0
    while ctrl <= 2:
        cripto = afdv.criptografarTexto(cdc.associacaoDeValores, cripto)
        ctrl += 1

    print(tdc.func_criptografar_coluna(cripto, 'C'))

def descriptografar():
    texto = input("Insira um texto para que possa ser Descriptografado:\n")

    cripto = tdc.func_criptografar_coluna(texto, 'D')
    ctrl = 0
    while ctrl <= 3:
        cripto = afdv.criptografarTexto(cdc.associacaoDeValoresVolta, cripto)
        ctrl += 1

    print(f'Seu Texto Descriptografado: {cripto}')
