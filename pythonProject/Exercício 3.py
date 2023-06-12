print('Cálculo do valor da conta de energia')

print('Qual o tipo de instalação é utilizada pelo cliente?')
print('R - Residência')
print('C - Comércio')
print('I - Indústria')

y = input('Digite o tipo de instalação (R,C ou I):')

x = float(input('Insira a quantidade de kWh consumidos:'))

z = float

if (y == 'R' and x <= 500):
    z = 0.40
elif (y == 'R' and x > 500):
    z = 0.65
elif (y == 'C' and x <= 1000):
    z = 0.55
elif (y == 'C' and x > 1000):
    z = 0.60
elif (y == 'I' and x <= 5000):
    z = 0.55
elif (y == 'I' and x > 5000):
    z = 0.60
else:
    print("Valor digitado inválido")

total = x * z

print('O valor do pagamento é de: R$ {}'.format(total))