# c = 1
# while c < 10:
#     print(c)
#     c += 1

# n = 1
# par = impar = 0
# while n != 0:
#     n = int(input('digite valor: '))
#     if n % 2 ==0:
#         par += 1
#     else:
#         impar += 1
# print(f'você digitou {par} pares e {impar} impares')

####### ler sexo 
# sexo = 'm' or 'f'
# while sexo == 'm' or sexo == 'f':
#     sexo = str(input('digite o seu sexo: ')).lower()
#     if sexo != 'm':
#         if sexo != 'f':
#             print('opçao invalida')

##### pensar em numero até acertar
# from random import randint
# pc = randint(0, 10)
# num = int(input('digite um numero: '))
# cont = 1
# while pc != num:
#     num = int(input('digite um numero: '))
#     cont += 1
#     if num < pc:
#         print('mais...')
#     elif num > pc:
#         print('menos')
# print(f'você acertou, o pc escolheu {pc}, foram necessarias {cont} tentativas')

##### ler dois valores e realizar a operação
# n1 = int(input('digite um valor: '))
# n2 = int(input('digite outro valor: '))
# op = 0

# while op != 5:
#     op = int(input('''[1]somar
# [2]multiplicar
# [3]maior
# [4]novos numeros
# [5]sair
# opção desejada: '''))
#     if op == 1:
#         soma = n1 + n2
#         print(f'a soma entre os numeros é {soma}')
#     if op == 2:
#         print(f'a multiplicação entre {n1} e {n2} é {n1*n2}')
#     if op == 3:
#         if n1 > n2:
#             print(f'o maior é {n1}')
#         else:
#             print(f'o maior é {n2}')
#     if op == 4:
#         n1 = int(input('digite um valor: '))
#         n2 = int(input('digite outro valor: '))
#     if op == 5:
#         print('final')
        
# print('fim')

####### fatorial
# from math import factorial
# num = int(input('digite um numero: '))
# print(f'o fatorial de {num} é {factorial(num)}')

### fatorial com while
# num = int(input('digite um numero: '))
# c = num
# f = 1
# while c > 0:
#     f *= c
#     c -= 1
# print(f)

##### PA
# n1 = int(input('digite um numero: '))
# razao = int(input('digite a razao: '))
# cont = 1
# t = n1

# while cont <= 10:
#     print(t)
#     t += razao
#     cont += 1

#### pa quantos termos quer mostrar
# n1 = int(input('digite um numero: '))
# razao = int(input('digite a razao: '))
# cont = 1
# t = n1
# total = 0
# termos = 10

# while termos != 0:
#     total = total + termos
#     while cont <= total:
#         print(t)
#         t += razao
#         cont += 1
#     termos = int(input('quantos termos quer mostrar: '))
# print('fim')

#### fribonacci
# num = int(input('digite um numero: '))
# seq = int(input('digite a sequencia: '))
# cont = 0
# f = [0]
# while cont <= seq:
#     print(num)
#     cont += 1
#     f.append(num)
#     num += f[-2]
##### fribonacci2
# seq = int(input('digite a sequencia: '))
# num = cont = 0
# f = 1
# while cont <= seq:
#     print(num)
#     print(f)
#     num += f
#     f += num
#     cont+=1


#### outro metodo
# n = int(input("Qual o tamanho da sequência de fibonacci você deseja ver? "))

# v0 = 0
# v = v1 = 1

# print(1)
# for i in range(n+1):
#     print(v)
#     v0 = v1
#     v1 = v
#     v = v0 + v1

###### leitura de numeros
# num = int(input('digite um numero: '))
# seguir = str(input('seguir [S/N]: ')).upper().strip()
# cont = soma = media = maior = menor = 0
# while seguir == 'S':
#     num = int(input('digite um numero: '))
#     seguir = str(input('seguir [S/N]: ')).upper().strip()
#     cont += 1
#     soma += num
#     media = (soma / cont)
#     if cont == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
# print(f'a média é {media:.2f}')
# print(f'o maior é {maior} o menor é {menor}')

