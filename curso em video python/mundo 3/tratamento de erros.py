#### verificar inteiro e real
# def leiaInt(msg):
#     while True:
#         try:
#               n = int(input(msg))
#         except (ValueError, TypeError):
#              print(f'erro, por favor digite um numero inteiro valido')
#              continue
#         except (KeyboardInterrupt):
#              print(f'entrade de dados interrompida pelo usuário')
#              return 0
#         else:
#              return n
        
# def leiafloat(msg):
#     while True:
#         try:
#               n = float(input(msg))
#         except (ValueError, TypeError):
#              print(f'erro, por favor digite um numero real valido')
#              continue
#         except (KeyboardInterrupt):
#              print(f'entrade de dados interrompida pelo usuário')
#              return 0
#         else:
#              return n

# n1 = leiaInt('digite um inteiro: ')
# n2 = leiafloat('digite um real: ')
# print(f'o valor inteiro foi {n1} e o real foi {n2}')


### verificação de site
# import urllib
# import urllib.error
# import urllib.request

# try:
#     site = urllib.request.urlopen('https://www.google.com.br')
# except urllib.error.URLError:
#     print('deu erro')
# else:
#     print('deu certo')