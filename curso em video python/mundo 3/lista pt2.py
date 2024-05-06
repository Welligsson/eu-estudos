#####pessoas e peso
# nome = []
# peso = []
# c = 0
# while True:
#     nome.append(str(input('nome: ')))
#     peso.append(int(input('peso: ')))
#     c += 1
#     r = str(input('quer continuar? [S/N]: '))
#     if r in 'Nn':
#         break

# print(f'você cadastrou {c} pessoas')
# print(f'O maior peso foi de {max(peso)}Kg. Peso de {nome[peso.index(max(peso))]}')
# print(f'O menor peso foi de {min(peso)}Kg. Peso de {nome[peso.index(min(peso))]}')

##### listas de pares e impares
# n = [[], []]
# for c in range (1, 8):
#     valor = int(input(f'digite o {c}° numero: '))
#     if valor % 2 == 0:
#         n[0].append(valor)
#     else:
#         n[1].append(valor)
# print('-' * 30)
# n[0].sort()
# n[1].sort()
# print(f'os valores pares digitados: {n[0]}')
# print(f'os valores impares digitados: {n[1]}')

# ### mega sena
# import random
# from time import sleep
# cont = int(input('quantos jogos sortear? '))
# c = 0
# print('=-'*20)
# while c < cont:
#     for i in range(cont):
#         pc = random.sample(range(1, 61), 6)
#     c += 1
#     pc.sort()
#     print(f'jogo {c}', pc)
#     sleep(0.5)
# print('=-'*20)

### matrizes
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range (0, 3):
#     for c in range (0, 3):
#         matriz[l][c] = int(input(f'digite o valor da matriz na posição [{l}, {c}]: '))
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()

#### matrizes melhoradas
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# spar = mai = scol = 0
# for l in range (0, 3):
#     for c in range (0, 3):
#         matriz[l][c] = int(input(f'digite o valor da matriz na posição [{l}, {c}]: '))
# print('=-'*20)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print()
# print('=-'*20)
# print(f'a soma dos pares é {spar}')
# for l in range (0, 3):
#     scol += matriz[l][2]
# print(f'a soma dos valores da treceira coluna é {scol}')
# for c in range(0, 3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]
# print(f'o maior valor da segunta linha é {mai}')

##### boletim
# ficha = list()
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = str(input('Quer continuar [S/N]? '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-' * 26)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-' * 35)
#     opc = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
#     if opc == 999:
#         print('FINALIZANDO...')
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')