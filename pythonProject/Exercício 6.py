#Calculadora com Laço de repetição(Tipo 1)

print('CALCULADORA')
total = float

z = input('Qual operação deseja fazer? ( + , - , * , / ):')
if (z == '+' or z == '-' or z == '*' or z == '/'):
    x = int(input('Digite o primeiro número:'))
    y = int(input('Digite o segundo número:'))


while(z != 's'):
    if (z == '+'):
        total = x + y
        print ('{} + {} é igual a {}'.format(x, y, total))
    elif(z == '-'):
         total = x - y
         print('{} - {} é igual a {}'.format(x, y, total))
    elif(z == '*'):
        total= x * y
        print('{} * {} é igual a {}'.format(x, y, total))
    elif(z == '/'):
        total = x / y
        print('{} / {} é igual a {}'.format(x, y, total))
    else:
        print ('Operção inválida')

    z = input('Qual operação deseja fazer? ( + , - , * , / ):')
    if (z == '+' or z == '-' or z == '*' or z == '/'):
        x = int(input('Digite o primeiro número:'))
        y = int(input('Digite o segundo número:'))

print('Encerrando programa.')
