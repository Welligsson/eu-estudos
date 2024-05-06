import os

carros = [
        ("Chevrolet Tracker", 120), 
        ("Chevrolet Onix", 90), 
        ("Chevrolet Spin", 150),
        ("Hyundai HB20", 85), 
        ("Hyundai Tucson", 120), 
        ("Fiat Uno", 60), 
        ("Fiat Mobi", 70), 
        ("Fiat Pulse", 130)
        ]
alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print(f'[{i}] {car[0]} - R$ {car[1]} /dia')

while True:
    os.system('cls')
    print('='*10)
    print('Bem vindo a locadora de carros')
    print('='*10)
    print('O que deseja fazer? ')
    op = int(input('0 - mostrar portfolio | 1 - alugar carro | 2 - devolver um carro: '))
    os.system('cls')
    if op == 0:
        mostrar_lista_de_carros(carros)
    elif op == 1:
        mostrar_lista_de_carros(carros)
        cod_car = int(input('Escolha o código do carro: '))
        dias = int(input('Por quantos dias deseja alugar este carro? '))
        os.system('cls')

        print(f'você escolheu o {carros[cod_car][0]} por {dias}')
        print(f'o aluguel totalizaria R$ {dias * carros[cod_car][1]}. Deseja alugar')
        conf = int(input('0 - SIM | 1 - NÃO: '))
        if conf == 0:
            print(f'parabens, você alugou o {carros[cod_car][0]} por {dias} dias')
            alugados.append(carros.pop(cod_car))
    elif op == 2:
        if len(alugados) == 0:
            print('Não há carros para devolver.')
        else:
            print('Segue a lista de carros alugados. Qual você deseja devolver?')
            mostrar_lista_de_carros(alugados)
            print()
            cod = int(input('escolha o código do carro que deseja devolver: '))
            if conf == 0:
                print(f'obrigado por devolver o carro {alugados[cod][0]}')
                carros.append(alugados.pop(cod))
    
    print('='*10)
    print('0 para CONTINUAR | 1 para SAIR')
    if float(input()) == 1:
        break