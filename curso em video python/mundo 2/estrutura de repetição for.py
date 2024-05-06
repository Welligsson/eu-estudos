#######contegem regressiva com tempo
# from time import sleep
# for c in range(10, 0, -1):
#     print(c)
#     sleep(1)
# print('fim!')

####### pares entre 1 e 50
# for c in range(0, 51, 2):
#     print(c)

###### soma de impares multiplos de 3 entre 1 a 500
# soma = 0
# for c in range(1, 501):
#     if c % 3 == 0 and c % 2 == 1:
#         soma += c
# print(f'a soma dos numero multiplos de 3 é igual a {soma}')

#### tabuada
# num = int(input('digite um numero: '))
# print(f'a tabuada de {num} é: ')

# for i in range(11):
#     print(f'{num} x {i} = {num * i}')

#### soma de numeros inteiros pares
# soma = 0
# for c in range(0, 6):
#     num = int(input('digite um numero: '))
#     if num % 2 == 0:
#         soma += num
# print(f' a soma dos numeros pares é {soma}')

##### ler numero e a razao de uma PA mostrando os 10 primeiros numeros
# num = int(input('digite um numero: '))
# razao = int(input('digite a razão da PA: '))

# for c in range(num, ((num + 10 -1)*razao)+razao, razao):
#     print(c)

#### numero primo
num = int(input('digite um numero: '))
c = 0
for i in range(1 , num + 1):
    if num % i == 0:
        c += 1

if c == 2:
    print('o numero é primo')
else:
    print('o numero nao é primo')

