# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'os resultados são {f1}, {f2}, {f3}')

# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input('digite um numero: '))
# if par(num):
#     print('é par!')
# else:
#     print('não é par!')

##### função voto
# def voto(ano):
#     from datetime import date
#     atual = date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return f'com {idade} anos: NÃO VOTA.'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'com {idade} anos: VOTO OPCIONAL.'
#     else:
#         return f'com {idade} anos: VOTO OBRIGATORIO.'

# nasc = int(input('Em que ano você nasceu? '))
# print(voto(nasc))

####Fatorial
# def fatorial(n, show=False):

#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:  
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f *= c
#     return f

# print(fatorial(5, show=True))

####jogadores
# def ficha(jog='<desconhecido>', gol=0):
#     print(f'o jogador {jog} fez {gol} gol(s) no campeonato')

# n = str(input('nome do jogador: '))
# g = str(input('numero de gols: '))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol=g)
# else:
#     ficha(n, g)

#### funçao leiaint
# def leiaint(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('ERRO! Digite um numero inteiro valido!')
#         if ok:
#             break
#     return valor

# n = leiaint('digite um numero: ')
# print(f'você acabou de digitar o numero {n}')

#####funçao notas
# def notas(*n, sit=False):
#     r = dict()
#     r['total'] = len(n)
#     r['maior'] = max(n)
#     r['média'] = sum(n)/len(n)
#     if sit:
#         if r['média'] >=  7:
#             r['situação'] = 'BOA'
#         elif r['média'] >= 5:
#             r['situação'] = 'RAZOAVEL'
#         else:
#             r['situação'] = 'RUIM'
#     return r


# resp = notas(5.5, 5.5, 9, 8.5, sit=True)
# print(resp)

####função de documentação
# def ajuda(com):
#     help(com)

# def titulo(msg, cor=0):
#     tam = len(msg) + 4
#     print('-' * tam)
#     print(f'  {msg}')
#     print('-' * tam)

# comando = ''
# while True:
#     titulo('SISTEMA DE AJUDA PyHELP')
#     comando = str(input('função ou biblioteca > '))
#     if comando.upper() == 'FIM':
#         break
#     else:
#         ajuda(comando)
# titulo('ATÉ LOGO')