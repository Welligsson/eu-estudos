# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# for c in range(0, len(lanche)):
#     print(lanche[c])

# for c in lanche:
#     print(f'eu vou comer {c}')

# for pos, c in enumerate(lanche):
#     print(f'{c} na {pos}')

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c)
# print(c.index(2))

### numeros de 0 a 20
# numero = ('zero', 'um', 'dois', 'tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
# while True:
#     dig = int(input('digite um numero de 0 a 20: '))
#     if 0 <= dig <= 20:
#         break
# print(f'você digitou o numero {numero[dig]}')

##### tupla random
# from random import randint as r

# tup = (r(0, 10), r(0, 10), r(0, 10), r(0, 10), r(0, 10))
# print(tup)
# print(f'maior {max(tup)}')
# print(f'menor {min(tup)}')
### ou 
# for c in range(0, len(tup)):
#     if c == 0:
#         menor = tup[c]
#         maior = tup[c]
#     else:
#         if tup[c] > maior:
#             maior = tup[c]
#         if tup[c] < menor:
#             menor = tup[c]
# print(f'o numero maior é {maior} e o numero menor é o {menor}')

###### guardar valores numa tupla
# a = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
# print(f'o valor 9 apareceu {a.count(9)} vezes')
# if a.count(3):
#     print(f'o valor 3 apareceu primeiro na {a.index(3)+1}° posição')
# else:
#     print('o valor 3 não apareceu nenhuma vez')
# print('os valores pares foram: ', end='')
# for c in a:
#     if c % 2 == 0:
#         print(c, end=', ')

#### listagem de preço
# listagem = ('Lápis', 1.75,
#             'Borracha', 2,
#             'Caderno', 15.9,
#             'Estojo', 25,
#             'Transferidor', 4.20,
#             'Compasso', 9.99,
#             'Mochila', 120.32,
#             'Canetas', 22.30,
#             'Livro', 34.90)
# print('-' * 40)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('-' * 40)
# for pos in range(0, len(listagem)):
#     if pos % 2 == 0:
#         print(f'{listagem[pos]:.<30}', end='')
#     else:
#         print(f'R${listagem[pos]:>7.2f}')
# print('-' * 40)


##### tupla palavras
# palavras = ('apreder', 'programar', 'linguagem', 'python', 'curso',
#             'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
#             'programador', 'futuro')
# for p in palavras:
#     print(f'na palavra {p} temos', end=' ')
#     for l in range(0, len(p)):
#         if p[l] in 'aeiou':
#             print(p[l], end=' ')
#     print()
