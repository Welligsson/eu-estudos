# #temperatura de c para f
# c = float(input('informe a temperatura em °C: '))
# f = 9 * c / 5 + 32

# print(f'a temperatura de {c}°C corresponde a {f}°F')

#aluguel de carros
dias = int(input('dias alugados: '))
km = float(input('kms rodados: '))

valordias = dias * 60
valorkm = km * 0.15

soma = valordias + valorkm

print(f'o valor total é R${soma:.2f}')
