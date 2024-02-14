import random
import sys
from time import sleep

#Função para imprimir as regras do jogo
def regras():
    print('-=' * 18)
    print('Estas são as regras do jogo: ', end='')
    print('''
1° Tesoura corta o papel
2° Papel cobre a pedra
3° Pedra esmaga o lagarto
4° Lagarto envenena o Spock
5° Spock quebra a tesoura
6° Tesoura decapita o lagarto
7° Lagarto come o papel
8° Papel refuta o Spock
9° Spock vaporiza a pedra
10° "e como sempre foi": Pedra esmaga a tesoura''')
    print('-=' * 18)

#Loop para o programa reinicar sempre que o jogador quiser, quando for perguntado a ele
while True:
    print('-' * 55)
    print('BEM VINDO AO JOGO DE PEDRA-PAPEL-TESOURA-LAGARTO-SPOCK!')
    print('-' * 55)

    p = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']

    print('''Digite:
[1] - Para ver as regras
[2] - Para começar a jogar
[3] - Para cancelar''')

    escolha = int(input('Escolha: '))

    if escolha == 1:
        regras()

        while True:
            escolha2 = input('Deseja voltar ao menu inicial? [S/N]: ').upper()[0]
            if escolha2 == 'N':
                print('Você saiu do jogo! Até a próxima!!')
                sys.exit() #Este comando encerra o programa
            elif escolha2 == 'S':
                break
            else:
                print('Escolha Inválida! Tente novamente.')


    elif escolha == 2:
        print('-=' * 18)
        print('Já pensei no que vou jogar!')
        print('Escolha a sua jogada de acordo com o numero que representa a palavra', end='')
        print('''
[1] - Pedra
[2] - Papel
[3] - Tesoura
[4] - Lagarto
[5] - Spock''')

        #Caso o jogador jogue qualquer numero que não esteja entre 1 e 5
        jogada = int(input('Sua Jogada: '))
        if jogada not in [1,2,3,4,5]:
            print('Jogada Inválida! Tente novamente.')

        #Fazer o programa escolher uma jogada
        pc = random.choice(p)

        #QUANDO O USUÁRIO GANHA
        if jogada == 3 and pc == 'Papel':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Tesoura corta o {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 2 and pc == 'Pedra':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Papel cobre a {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 1 and pc == 'Lagarto':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Pedra esmaga o {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 4 and pc == 'Spock':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Lagarto envenena o {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 5 and pc == 'Tesoura':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Spock quebra a {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 3 and pc == 'Lagarto':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Tesoura decapita o {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 4 and pc == 'Papel':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Lagarto come o {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 2 and pc == 'Spock':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Papel refuta o {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 5 and pc == 'Pedra':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Spock vaporiza a {pc}, portanto: VOCÊ GANHOU!')
        if jogada == 1 and pc == 'Tesoura':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Pedra esmaga a {pc}, portanto: VOCÊ GANHOU!')

        #QUANDO O PC GANHA
        if jogada == 2 and pc == 'Tesoura':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Tesoura corta o papel, portanto: EU GANHEI!')
        if jogada == 1 and pc == 'Papel':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Papel cobre a pedra, portanto: EU GANHEI!')
        if jogada == 4 and pc == 'Pedra':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Pedra esmaga o lagarto, portanto: EU GANHEI!')
        if jogada == 5 and pc == 'Lagarto':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Lagarto envenena o Spock, portanto: EU GANHEI!')
        if jogada == 3 and pc == 'Spock':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Spock quebra a tesoura, portanto: EU GANHEI!')
        if jogada == 4 and pc == 'Tesoura':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Tesoura decapita o lagarto, portanto: EU GANHEI!')
        if jogada == 2 and pc == 'Lagarto':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Lagarto come o papel, portanto: EU GANHEI!')
        if jogada == 5 and pc == 'Papel':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Papel refuta o Spock, portanto: EU GANHEI!')
        if jogada == 1 and pc == 'Spock':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Spock vaporiza a pedra, portanto: EU GANHEI!')
        if jogada == 3 and pc == 'Pedra':
            sleep(1.30)
            print(f'Eu escolhi "{pc}", Pedra esmaga a tesoura, portanto: EU GANHEI!')

        #QUANDO DER EMPATE
        if jogada == 1 and pc == 'Pedra':
            sleep(1.30)
            print(f'Eu também escolhi "{pc}", portanto: EMPATAMOS!')
        if jogada == 2 and pc == 'Papel':
            sleep(1.30)
            print(f'Eu também escolhi "{pc}", portanto: EMPATAMOS!')
        if jogada == 3 and pc == 'Tesoura':
            sleep(1.30)
            print(f'Eu também escolhi "{pc}", portanto: EMPATAMOS!')
        if jogada == 4 and pc == 'Lagarto':
            sleep(1.30)
            print(f'Eu também escolhi "{pc}", portanto: EMPATAMOS!')
        if jogada == 5 and pc == 'Spock':
            sleep(1.30)
            print(f'Eu também escolhi "{pc}", portanto: EMPATAMOS!')

        #Loop para quando o jogo acabar, e perguntar se o jogador quer continuar ou não
        while True:
            escolha2 = str(input('Deseja voltar ao menu inicial? [S/N]: ')).upper()[0]
            if escolha2 == 'N':
                print('Você saiu do jogo! Até a próxima!!')
                sys.exit()
            elif escolha2 == 'S':
                break
            else:
                print('Escolha Inválida! Tente novamente.')
                break

    elif escolha == 3:
        print('Jogo Cancelado. Até a próxima!')
        break
    #pro caso dele digitar um numero inválido (que seja != de 1, 2 e 3)
    else:
        print('Escolha inválida. Tente novamente.')