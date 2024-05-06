import os

operations = {
    '+': 'soma',
    '-': 'subtração',
    '*': 'multiplicação',
    '/': 'divisão',
    '**': 'exponenciação'
}

while True:
    os.system('cls')
    i = 0
    print('-=' * 10)
    for op, name in operations.items():
        
        print(i, ':', name)
        i += 1
    print('-=' * 10)
    print('Escolha a opção que deseja realizar: ')
    op = int(input())
    op_string = list(operations.keys())[op]
    print()
    print(f'{op_string} escolhida')
    print()
    print('qual o primeiro valor? ')
    v1 = float(input())
    print('qual o segundo valor? ')
    v2 = float(input())

    if op == 0:
        r = v1 + v2
    elif op == 1:
        r = v1 - v2
    elif op == 2:
        r = v1 * v2
    elif op == 3:
        r = v1 / v2
    elif op == 4:
        r = v1 ** v2

    print()
    print(f'a {v1} {op_string} {v2} = {r}')
    print('-=' * 10)
    print('deseja realizar mais alguma operação? (digite 1 para sair)')
    comando = int(input())
    if comando == 1:
        break

