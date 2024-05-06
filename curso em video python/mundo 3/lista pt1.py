# valores = []
# for cont  in range(0, 5):
#     valores.append(int(input('digite um valor: ')))

# for c, v in enumerate(valores):
#     print(f'na posição {c} encontrei o valor {v}!')
# print('cheguei ao final da lista')

# a = [2, 3, 4, 7]
# b = a[:] ---> cria copia da lista
# b[2] = 8
# print(f'lista a: {a}')
# print(f'lista a: {b}')

# #### ler valores e verificar
# valores = []
# for cont  in range(0, 5):
#     valores.append(int(input('digite um valor: ')))
# print(f'maior {max(valores)} na posição {valores.index(max(valores))}')
# print(f'menor {min(valores)} na posição {valores.index(min(valores))}')

#####adicionar valores na lista
# l = []
# while True:
#     n = int(input('Digite um valor inteiro pra ser adicionado: '))
#     s = str(input('quer continuar? [S/N] ')).lower()
#     if s == 'n':
#         break
#     if n in l:
#         print('este numero ja exite na lista!')
#     else:
#         l.append(n)
# l.append(n)
# l.sort()
# print(l)

#### adicionar valores no lugar correto
# l = []
# for c in range(0, 5):
#     n = (int(input('digite um valor: ')))
#     if c == 0 or n > l[-1]:
#         l.append(n)
#         print('Adicionado no final da lista')
#     else:
#         pos = 0
#         while pos < len(l):
#             if n <= l[pos]:
#                 l.insert(pos, n)
#                 print(f'adicionado na posição {pos} da lista')
#                 break
#             pos += 1
# print('-=' * 30)
# print(f'Os valores digitados em ordem foram {l}')

###### mais uma verificação de lista
# l = []
# for c in range(0, 5):
#     l.append(int(input('digite um valor: ')))
#     l.sort(reverse=True)
# print(f'foram digitados {c+1} valores na lista')
# print(f'em ordem decrescente {l}')
# if 5 in l:
#     print('o valor 5 existe na lista')
# else:
#     print('não existe valor 5')

##### listas de pares e impares
# l = []
# p = []
# i = []

# for c in range(0, 5):
#     n = int(input('digite um valor: '))
#     l.append(n)
#     l.sort()
#     if n % 2 == 0:
#         p.append(n)
#         p.sort()
#     else:
#         i.append(n)
#         i.sort()
# print(f'a lista é {l}')
# print(f'valores pares {p}')
# print(f'valores impares {i}')

##### expressao
# expr = str(input('digite a expressao: '))
# pilha = []
# for simb in expr:
#     if simb == '(':
#         pilha.append('(')
#     elif simb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('sua expressaõ é valida!')
# else:
#     print('sua expressão é invalida!')