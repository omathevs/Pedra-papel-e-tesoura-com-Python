from random import randint

def tabela():
    print('''
[1] Pedra
[2] Papel
[3] Tesoura''')

jogada = (None, 'Pedra', 'Papel', 'Tesoura')

while True:
    tabela()
    computador = randint(1, 3)

    try:
        jogador = int(input('\nJogue: '))
        print()
        print(f'Você: {jogada[jogador]}')
        print(f'Computador: {jogada[computador]}\n')

        if computador == 1:
            if jogador == 2:
                print('Você venceu!')
            elif jogador == 3:
                print('Computador venceu!')
            elif jogador == 1:
                print('Empate.')

        if computador == 2:
            if jogador == 3:
                print('Você venceu!')
            elif jogador == 1:
                print('Computador venceu!')
            elif jogador == 2:
                print('Empate.')
                
        if computador == 3:
            if jogador == 1:
                print('Você venceu!')
            elif jogador == 2:
                print('Computador venceu!')
            elif jogador == 3:
                print('Empate.')

        continuar = ' '
        while continuar not in 'SsNn':
            continuar = input('\nDeseja continuar? [S/N]\n').upper()[0]
            if continuar not in 'SsNn':
                print('Informe uma entrada válida.')
        if continuar == 'N':
            break

    except IndexError:
        print('Jogada inválida! Informe um valor válido.')
    except ValueError:
        print('Informe um valor válido.')
