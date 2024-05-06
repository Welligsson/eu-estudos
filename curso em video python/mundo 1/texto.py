######leitura de nome
# nome = input('nome: ')

# print(nome.upper())
# print(nome.lower())
# print(len(nome.replace(' ',''))) #qtd sem espaços
# print(len(nome.split()[0])) #qtd primeiro nome

###### mostrar digitos
# num = int(input('numero de 0 a 9999: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'unidade: {u}')
# print(f'dezena: {d}')
# print(f'centena: {c}')
# print(f'milhar: {m}')

###### ler nome de cidade que começa com santo
# cid = str(input('cidade: ').strip())
# print(cid[:5].upper() == 'SANTO')

# #### nome se tem silva
# nome = input('nome: ')
# print('SILVA' in nome.upper())

##### verificar letra A
# frase = input('frase: ').upper().strip()
# print(frase.count('A'))
# print(frase.find('A') + 1)
# print(frase.rfind('A') + 1)

#### primeiro e ultimo nome
# nome = input('nome completo: ').strip()
# print(f'seu primeiro nome é {nome.split()[0]}')
# print(f'seu ultimo nome é {nome.split()[-1]}')
# print(nome.split()[0], nome.split()[-1])