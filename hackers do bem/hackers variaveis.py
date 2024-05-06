# entrada de dados
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
idade = int(input('digite sua idade: '))

# processamento

imc = peso/(altura*altura)
print(f'seu imc é igual a : {imc:.2f} e a sua idade é igual a {idade}')