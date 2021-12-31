def leiaInt(msg):
    ok = True
    while ok:
        try:
            numero = int(input(msg))
        except KeyboardInterrupt:
            print('O usuário preferiu encerrar com o programa manualmente.')
            ok = False
        except:
            print('Digite um número INTEIRO válido.')
        else:
            if numero > 10:
                print('Por favor, digite um número entre 0 e 10.')
            elif numero < 0:
                print('Por favor, digite um número maior que 0.')
            else:
                return numero


def tentativa(numero_digitado, numero_aleatorio):
    if numero_digitado == numero_aleatorio:
        print('Parabéns!! Você conseguiu acertar o número em que pensei com 1 tentativa!!! Incrível!')
        return numero_digitado
    elif numero_digitado < numero_aleatorio:
        print('Hm... Não foi esse! O número que pensei é MAIOR que o digitado. Tente novamente!')
    elif numero_digitado > numero_aleatorio:
        print('Eita! Esse não foi o número que pensei! Na verdade, ele é um número MENOR que esse digitado!')
