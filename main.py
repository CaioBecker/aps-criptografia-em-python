from pickle import TRUE

import FuncoesDeCriptografia as aps

while TRUE:
    opcao = input('Criptografar-1 / Descriptografar-2\n')
    
    if opcao == '1' or opcao == '2':
        if opcao == '1':
            aps.criptografar()
        else:
            aps.descriptografar()

#VALORES PARA TESTES
#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"!@#$%&*()-_=+§{[ª}]º^|<,>.:;?/çãõÇÃÕ
#2xdesc5f80zuT5Juu954!y2!Jt58f5qJSJy5sRu81uJJu8Vu44qJt58S590u