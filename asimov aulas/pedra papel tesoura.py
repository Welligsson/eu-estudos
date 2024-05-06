import random
import os

move_list = ['papel', 'pedra', 'tesoura']
player_count = 0
computer_count = 0

print('=' * 20)
print('BEM VINDO AO JOGO PAPEL, PEDRA E TESOURA')

def main_print():
    print('=' * 20)
    print('\nPLACAR:')
    print(f'você: {player_count}')
    print(f'computador: {computer_count}')
    print()
    print('escolha seu lance: ')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]
        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count
    if p_move == 'papel':
        if c_move == 'pedra':
            player_count += 1
            return 'p'
        elif c_move == 'tesoura':
            computer_count += 1
            return 'c'
        else:
            return 'd'
        
    if p_move == 'pedra':
        if c_move == 'tesoura':
            player_count += 1
            return 'p'
        elif c_move == 'papel':
            computer_count += 1
            return 'c'
        else:
            return 'd'
        
    if p_move == 'tesoura':
        if c_move == 'papel':
            player_count += 1
            return 'p'
        elif c_move == 'pedra':
            computer_count += 1
            return 'c'
        else:
            return 'd'

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)
    print()
    print('=' * 20)
    print(f'Sua jogada {player_move.upper()}')
    print(f'jogadad do computador: {computer_move.upper()}')

    if winner == 'p':
        print('Você venceu!')
    if winner == 'c':
        print('Você perdeu!')
    else:
        print('Empate')
    print('=' * 20)

    while True:
        next = int(input('jogar novamente? 0 - sim | 1 - não: '))
        if next == 0:
            break
        elif next == 1:
            again = 0
            break
    os.system('cls')