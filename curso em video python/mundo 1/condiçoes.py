import random
from datetime import date
####### numero de 0 a 5
# num = int(input('digite um numero de 0 a 5: '))
# r = int(random.randint(0,5))

# if num == r:
#     print('parabéns, você acertou')
# else:
#     print(f'você errou o numero esolhido era {r}')

# print('fim!')

#### limite de velocidade
# v = float(input('digite a velocidade: '))

# if v <= 80:
#     print('dentro do limite de velociade')
# else:
#     print('você ultrapassou o limite de velocidade!!')
#     multa = (7 * (v - 80))
    # print(f'a multa será no valor de R${float(multa)}')

#### par impar
# n = int(input('digite um numero inteiro: '))
# if n % 2 == 1:
#     print(f'o numero {n} é impar!')
# else:
#     print(f'o numero {n} é par!')


### valor da passagem
# d = float(input('distancia da viagem: '))
# if d <= 200:
#     preco = d * 0.5
#     print(f'o valor da passagem será R$ {preco}')
# else:
#     preco = d *0.45
#     print(f'o valor da passagem será R$ {preco}')

#### ano bissexto
# ano = int(input('digite o ano em que estamos, coloque 0 para analisar o ano atual: '))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
#     print(f'o ano {ano} é bissexto!')
# else:
#     print(f'o ano {ano} não é bissexto!')

##### maior e menor
# a = float(input('digite um numero: '))
# b = float(input('digite um numero: '))
# c = float(input('digite um numero: '))

# if a > b and a > c:
#     print(f'o maior é {a}')
# if b > a and b > c:
#     print(f'o maior é {b}')
# if c > a and c > b:
#     print(f'o maior é {c}')

# if a < b and a < c:
#     print(f'o menor é {a}')
# if b < a and b < c:
#     print(f'o menor é {b}')
# if c < a and c < b:
#     print(f'o menor é {c}')

#### salario
# s = float(input('digite o seu salario: '))
# if s >= 1250:
#     s = s + (s * 10/100)
#     print(f'seu salario agora será {s}')
# else:
#     s = s + (s * 15 / 100)
#     print(f'seu salario agora será {s}')

### possibilidade de triangulo
l1 = int(input('digite um valor: '))
l2 = int(input('digite um valor: '))
l3 = int(input('digite um valor: '))

if (l1 + l2) > l3  and (l1 + l3) > l2 and (l2 + l3) > l1:
    print(f'é possivel formar um triangulo: ')

else:
    print('não é possivel formar um triangulo')
