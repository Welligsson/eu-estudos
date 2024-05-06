# def lin():
#     print('-' * 50)

# lin()
# print('Vou aprender python EM NOME DO SENHOR JESUS')
# lin()

# def titulo(txt):
#     print('-' * 50)
#     print(txt)
#     print('-' * 50)

# titulo('Vou aprender python EM NOME DO SENHOR JESUS')
# titulo('Olá, mundo!')
# def soma(a, b):
#     s = a + b
#     print(s)

# soma(4, 5)
# soma(8, 9)
# soma(2, 1)

# def contador(* num):
#     print(len(num))

# contador(2,0,5)
# contador(3,2)
# contador(4,4,7,6,2)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos +=1

# valores = [6,3,5,2,4]
# dobra(valores)
# print(valores)

# def soma(* valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'somando os valores {valores} temos {s}')

# soma(5,2)
# soma(2,9,4)

###### largura de terreno
# def area(larg, comp):
#     a = larg * comp
#     print(f'a área de um terreno {larg}x{comp} é de {a}m²')

# print('  controle de terrenos  ')
# print('-' *20)
# l = float(input('largura (m): '))
# c = float(input('comprimento (m): '))
# area(l, c)

#######funçao escreva
# def escreva(msg):
#     tam = len(msg) + 4
#     print('~' * tam)
#     print(f'  {msg}')
#     print('~' * tam)

# escreva('Welligsson Coutinho')
# escreva('Deus seja louvado')

##### funçao de contagem
# from time import sleep
# def contador(i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print('-' * 20)
#     print(f'contagem de {i} até {f} de {p} em {p}')
#     sleep(2)
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end='')
#             sleep(0.1)
#             cont += p
#         print('FIM!')
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='')
#             sleep(0.1)
#             cont -= p
#         print('FIM!')
#     print('-' * 20)

# contador(1, 10, 1)
# contador(10, 0, 2)
# print('agora é sua vez!')
# print('-' * 20)
# ini = int(input('INICIO: '))
# fim = int(input('fim: '))
# passo = int(input('passo: '))
# contador(ini, fim, passo)

#####funçao verificar o maior de varios valores
# from time import sleep
# def maior(* num):
#     cont = maior = 0
#     print('-' * 20)
#     print('analisando os valores passados...')
#     for valor in num:
#         print(f'{valor} ', end='')
#         sleep(0.2)
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont += 1
#     print(f'foram informados {cont} valores ao todo')
#     print(f'o maior valor informado foi {maior}')

# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()

#####listas e funçoes
# from random import randint
# from time import sleep
# def sorteia(lista):
#     print('SORTEANDO 5 VALORES NA LISTA')
#     for cont in range(0, 5):
#         n = randint(1, 10)
#         lista.append(n)
#         print(f'{n} ', end='')
#         sleep(0.2)
#     print('PRONTO!')

# def somaPar(lista):
#     soma = 0
#     for valor in lista:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'somando os valores pares da {lista}, temos {soma}')

# num = list()
# sorteia(num)
# somaPar(num)