### valor casa
# vc = float(input('valor da casa: '))
# vs = float(input('salario: '))
# anos = int(input('em quantos anos vai pagar: '))

# parcelas = vc / anos / 12

# if parcelas >= (vs/10*3) :
#     print('você não poderá comprar a casa')
#     print('valor das parcelas excedem a 30%' ' do salario')
# else:
#     print(f'você pagará R${float(parcelas):.2f}')

###### transformação de base
# n = int(input('digite um inteiro: '))
# base = int(input('digite 1 para converter em binario, 2 para octal e 3 para hexadecimal: '))

# if base == 1:
#     n = bin(n)[2:]
#     print(n)
# elif base == 2:
#     n = oct(n)[2:]
#     print(n)
# elif base == 3:
#     n = hex(n)[2:]
#     print(n)

###### comparação de numeros
# n1 = float(input('digite um numero: '))
# n2 = float(input('digite outro numero: '))

# if n1 > n2:
#     print(f'{n1} é maior que {n2}')
# elif n2 > n1:
#     print(f'{n2} é maior que {n1}')
# else:
#     print('os numeros são iguais')

##### alistamento
# from datetime import date
# ano = int(input('digite o ano de nascimento: '))

# if date.today().year - ano == 18:
#     print('você deve se alistar')
# elif date.today().year - ano < 18:
#     faltam_anos = date.today().year - 18 - ano
#     print(f'você deverá se alistar em {(faltam_anos * (-1))} anos')
# elif date.today().year - ano > 18:
#     faltam_anos = date.today().year - 18 - ano
#     print(f'você ja passou {faltam_anos} anos do alistamento')

#### media nota
# n1 = float(input('digite nota 1: '))
# n2 = float(input('digite nota 2: '))
# media = (n1 + n2) / 2

# if media < 5.0:
#     print(f'sua média foi {media:.1f}. REPROVADO!')
# elif media >= 5 and media <= 6.9:
#     print(f'sua média foi {media:.1f}. RECUPERAÇÃO!')
# elif media >= 7:
#     print(f'sua média foi {media:.1f}. APROVADO!')

##### CATEGORIA NATAÇÃO
# from datetime import date
# ano = int(input('digite o ano de nascimento: '))

# if date.today().year - ano <= 9:
#     print('categoria MIRIM')
# elif date.today().year - ano <= 14:
#     print('categoria INFANTIL')
# elif date.today().year - ano <= 19:
#     print('categoria JUNIOR')
# elif date.today().year - ano <= 25:
#     print('categoria SENIOR')
# elif date.today().year - ano > 25:
#     print('categoria MASTER')

##### verificação triangulo
# l1 = int(input('digite um valor: '))
# l2 = int(input('digite um valor: '))
# l3 = int(input('digite um valor: '))

# if (l1 + l2) > l3  and (l1 + l3) > l2 and (l2 + l3) > l1:
#     print(f'é possivel formar um triangulo: ')
#     if l1 == l2 == l3:
#         print('triangulo equilatero')
#     elif l1 == l2 or l2 == l3 or l1 == l3:
#         print('triangulo isoceles')
#     else:
#         print('triangulo escaleno!')
# else:
#     print('não é possivel formar um triangulo')

#### desconto
# v = float(input('valor do produto: '))
# pgt = int(input('digite 1 para pagamento em dinheiro, 2 para cartão, 3 para em 2x no cartão, 4 para 3x no cartão: '))

# if pgt == 1:
#     vr = v - (v * 10/100)
#     print(f'o valor do produto será R${vr}')
# elif pgt == 2:
#     vr = v - (v * 5/100)
#     print(f'o valor do produto será R${vr}')
# elif pgt == 3:
#     print(f'o valor do produto será R${v}')
# elif pgt == 4:
#     vr = v + (v * 20/100)
#     print(f'o valor do produto será R${vr}')


#### jokenpo
# import random
# itens = ['Pedra', 'Papel', 'Tesoura']
# jogador = int(input('''[0] pedra
# [1] papel
# [2] tesoura
# Qual sua jogada? '''))
# pc = random.randint(0 , 2)

# match pc:
#     case 0:
#         match jogador:
#             case 0:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('empate')
#             case 1: 
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('venceu')
#             case 2:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('perdeu')
#     case 1:
#         match jogador:
#             case 0:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('perdeu')
#             case 1:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('empate')
#             case 2:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('venceu')
#     case 2:
#         match jogador:
#             case 0:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('venceu')
#             case 1:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('perdeu')
#             case 2:
#                 print(f'mao escolhida pelo jogador {itens[jogador]}')
#                 print(f'mao escolhida pelo pc {itens[pc]}')
#                 print('empate')
    
import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
b = random.randint(1,3)
print (b)
if a == b:
    print ("EMPATE")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")