#### média aluno 
# aluno = {}
# aluno['aluno'] = input('Digite o nome do aluno: ')
# aluno['media'] = float(input('Digite a média do aluno: '))

# print(f'O aluno {aluno["aluno"]} tem nota {aluno["media"]}')

# if aluno['media'] >= 6:
#     print('Aluno aprovado')
# else:
#     print('Aluno reprovado')


#### colocar random em dicionarios, jogo de dados
# from random import randint
# from time import sleep
# from operator import itemgetter
# jogo = {
#     'jogador1': randint(1, 6),
#     'jogador2': randint(1, 6),
#     'jogador3': randint(1, 6),
#     'jogador4': randint(1, 6),
# }
# ranking = []
# print('valores sorteados: ')
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('-=' * 30)
# print('  == RANKING DOS JOGADORES ==')
# for i, v in enumerate(ranking):
#     print(f'  {i+1}° lugar {v[0]} com {v[1]} ')
#     sleep(1)

##### ADICIONANDO VALORES EM UM DICIONARIO
# from datetime import datetime
# dados = dict()
# dados['nome'] = str(input('nome: '))
# nasc = int(input('ano de nascimento: '))
# dados['idade'] = datetime.now().year - nasc
# dados['ctps'] = int(input('carteira de trabalho (0 não tem): '))
# if dados['ctps'] != 0:
#     dados['contratação'] = int(input('ano de contratação: '))
#     dados['salario'] = float(input('salario: R$'))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
# print('-=' * 30)
# for k, v in dados.items():
#     print(f'{k} tem valor {v}')

##### Jogadores
# jogador = dict()
# partidas = list()
# jogador['nome'] = str(input('nome do jogador: '))
# tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#     partidas.append(int(input(f'quantos gols na partida {c}? ')))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# for k, v in jogador.items():
#     print(f'o campo {k} tem o valor {v}')
# print('-=' * 30)
# print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
# for i, v in enumerate(jogador['gols']):
#     print(f' => na partida {i}, fez {v} gols')
# print(f'foi um total de {jogador["total"]} gols')

##### unindo dicionarios a listas
# galera = list()
# pessoa = dict()
# soma = media = 0
# while True:
#     pessoa.clear()
#     pessoa['nome'] = str(input('nome: '))
#     while True:
#         pessoa['sexo'] = str(input('sexo: [M/F] ')).upper()[0]
#         if pessoa['sexo'] in 'MF':
#             break
#         print('ERRO! DIGITE APENAS M ou F')
#     pessoa['idade'] = int(input('idade: '))
#     soma += pessoa['idade']
#     galera.append(pessoa.copy())
#     while True:
#         resp = str(input('quer continuar? [S/N] ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('ERRO! RESPONDA APENAS S ou N')
#     if resp == 'N':
#         break
# print('-=' * 30)
# print(f'ao todo temos {len(galera)} pessoas cadastradas')
# media = soma / len(galera)
# print(f'a media de idade é de {media:5.2f} anos.')
# print('as mulheres cadastradas foram ', end='')
# for p in galera:
#     if p['sexo'] in 'Ff':
#         print(f'{p['nome']} ', end='')
# print()
# print(' lista das pessoas que estão acima da media: ')
# for p in galera:
#     if p['idade'] >= media:
#         print('    ', end='')
#         for k, v in p.items():
#             print(f'{k} = {v}; ', end='')
#         print()
# print('ENCERRADO!!!')

##### jogadores melhorado
# jogador = dict()
# partidas = list()
# time = list()
# while True:
#     jogador.clear()
#     jogador['nome'] = str(input('nome do jogador: '))
#     tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
#     partidas.clear()
#     for c in range(0, tot):
#         partidas.append(int(input(f'quantos gols na partida {c+1}? ')))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     time.append(jogador.copy())
#     while True:
#         resp = str(input('quer continuar? [S/N] ')).upper()[0]
#         if resp in 'SN' :
#             break
#         print('ERRO! RESPONDA APENAS S ou N')
#     if resp == 'N':
#         break
# print('-' * 40)
# print('cod ', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
# print('-' * 40)
# for k, v in enumerate(time):
#     print(f'{k:>3} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-' * 40)
# while True:
#     busca = int(input('mostrar dados de qual jogador? (999 p/ parar) '))
#     if busca == 999:
#         break
#     if busca >= len(time):
#         print(f'ERRO! Não existe jogador com código {busca}')
#     else:
#         print(f' --LEVANTAMENDO DO JOGADOR {time[busca]["nome"]}: ')
#         for i, g in enumerate(time[busca]['gols']):
#             print(f'    no jogo {i+1} fez {g} gols')
#     print('-'*40)
# print('volte sempre!!!')