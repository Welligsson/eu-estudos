import random
itens = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input('''[0] pedra
[1] papel
[2] tesoura
Qual sua jogada? '''))
pc = random.randint(0 , 2)

match pc:
    case 0:
        match jogador:
            case 0:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('empate')
            case 1: 
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('venceu')
            case 2:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('perdeu')
    case 1:
        match jogador:
            case 0:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('perdeu')
            case 1:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('empate')
            case 2:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('venceu')
    case 2:
        match jogador:
            case 0:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('venceu')
            case 1:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('perdeu')
            case 2:
                print(f'mao escolhida pelo jogador {itens[jogador]}')
                print(f'mao escolhida pelo pc {itens[pc]}')
                print('empate')