#Maneira 1 de executar

valor = int(input('Digite o valor que deseja em R$:'))

if (valor >= 100):
    cedulas100 = valor // 100
    valor = valor - cedulas100 * 100
    print('Cédula(s) de R$100: {}.'.format(cedulas100))

if (valor >= 50):
    cedulas50 = valor // 50
    valor = valor - cedulas50 * 50
    print('Cédula(s) de R$50: {}.'.format(cedulas50))

if (valor >= 20):
    cedulas20 = valor // 20
    valor = valor - cedulas20 * 20
    print('Cédula(s) de R$20: {}.'.format(cedulas20))

if (valor >= 10):
    cedulas10 = valor // 10
    valor = valor - cedulas10 * 10
    print('Cédula(s) de R$10: {}.'.format(cedulas10))

if (valor >= 5):
    cedulas5 = valor // 5
    valor = valor - cedulas5 * 5
    print('Cédula(s) de R$5: {}.'.format(cedulas5))

if valor:
    cedulas1 = valor
    print('Cédula(s) de R$1: {}.'.format(cedulas1))