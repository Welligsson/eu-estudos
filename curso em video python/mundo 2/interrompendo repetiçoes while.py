#### ler numeros e parar com 999
# n = cont = media = soma = maior = menor = 0
# while True:
#     n = int(input('numero: '))
#     if n == 999:
#         break
#     cont += 1
#     soma += n
#     if cont == 1:
#         maior = menor = n
#     else:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
# media = soma / cont
# print(f'a média dos numeros foi {media}')
# print(f'o maior é {maior} o menor é {menor}')


### mostrar tabuadas
# n = 0
# while True:
#     n = int(input('tabuada: '))
#     if n < 0 :
#         break
#     for i in range(11):
#         print(f'{n} x {i} = {n * i}')
#     print()
# print('fim')

#### par impar
# from random import randint
# v = 0
# while True:
#     n = int(input('digite um numero: '))
#     pc = randint(1,10)
#     mao = ' '
#     while mao not in 'PI':
#         mao = str(input('par ou impar [P/I]: ')).upper(). strip()[0]
#     print(f'você jogou {n} e o computador {pc}')
#     if mao == 'P':
#         if (n + pc) % 2 == 0:
#             print(f'total {n + pc} deu par, você venceu!!!')
#             v += 1
#         else:
#             print('você perdeu!!!')
#             break
#     if mao == 'I':
#         if (n + pc) % 2 == 1:
#             print(f'total {n + pc} deu impar, você venceu!!!')
#             v += 1
#         else:
#             print('você perdeu!!')
#             break

#### verificar grupo
# resp = 's'
# cont = conthomem = maioridadehomem = totmulher = somaidade = 0
# nomevelho = ''
# while resp not in 'Nn':
#     cont += 1
#     nome = str(input('nome: ')).strip()
#     idade = int(input('idade: '))
#     sexo = str(input('sexo [M/F]: ')).strip()
#     resp = str(input('quer continuar? [S/N]')).strip().upper()
#     somaidade += idade
#     if sexo in 'Mm':
#         conthomem +=1
#     if sexo in 'Mm' and idade >= 18:
#         maioridadehomem += 1
#     if sexo in 'Ff' and idade < 20:
#         totmulher += 1
# mediaidade = somaidade / cont
# print(f'a media de idade do geupo é {mediaidade:.2f} anos')
# print(f'possuem {maioridadehomem} homens maiores de 18 anos')
# print(f'possuem {totmulher} abaixo de 20 anos')


"""
EXERCÍCIO 070: Estatísticas em Produtos

Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
# total = totmil = menor = cont = 0
# barato = ''
# while True:
#     produto = str(input('Nome do produto: '))
#     preco = float(input('Preço: R$ '))
#     cont += 1
#     if cont == 1 or preco < menor:
#         menor = preco
#         barato = produto
#     total += preco
#     if preco > 1000:
#         totmil += 1
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'{" FIM DO PROGRAMA ":-^40}')
# print(f'O total da compra foi R$ {total:.2f}')
# print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
# print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')


"""
EXERCÍCIO 071: Simulador de Caixa Eletrônico

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""
# print('=' * 30)
# print(f'{"BANCO CEV":^30}')
# print('=' * 30)
# valor = int(input('Que valor você quer sacar? R$ '))
# total = valor
# ced = 50
# totced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         totced += 1
#     else:
#         if totced > 0:
#             print(f'Total de {totced} cédulas de R$ {ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totced = 0
#         if total == 0:
#             break
# print('=' * 30)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!')