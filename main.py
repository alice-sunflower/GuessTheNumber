#Criar um programa que sorteia um número aleatório e pede para o usuário tentar acertar

#Importar função RANDINT para sortear um número aleatório // Importar função LEIAINT para ler um número inteiro corretamente 
#Importar função TENTATIVA para chutar o número
from random import randint
from modulos import leiaInt, tentativa

#Variável NUMERO_SORTEADO receberá o valor sorteado entre 0 e 10 // Variável CHUTE receberá um valor inteiro digitado pelo usuário
#Variável CONTADOR para determinar quantas tentativas o usuário usou até acertar o número (Começa em 1 por conta da função tentativa já utilizar 1)
numero_sorteado = randint(0, 10)
chute = leiaInt('Pensei em um número! Tente acertá-lo... Digite um número entre 0 e 10: ')
contador = 1

#Variável V que recebe TENTATIVA para verificar no LOOP se o número é igual ou diferente do número que foi sorteado
v = tentativa(chute, numero_sorteado)

#Loop para verificar se o valor digitado é o mesmo do valor sorteado 
if v != numero_sorteado:
    while True:
        chute = leiaInt('Tente novamente! Digite um número entre 0 e 10: ')
        contador += 1
        if chute == numero_sorteado:
            print(f'Parabéns!! Você conseguiu acertar o número em que pensei com {contador} tentativas!')
            break
        elif chute < numero_sorteado:
            print('Hm... Não foi esse! O número que pensei é MAIOR que o digitado.')
        elif chute > numero_sorteado:
            print('Eita! Esse não foi o número que pensei! Na verdade, ele é um número MENOR que esse digitado!')
else:
    print('Obrigado por ter jogado!')
