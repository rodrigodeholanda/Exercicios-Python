#Calculadora com Laço de repetição (Tipo 2)

print('CALCULADORA')

while True:
    total = float
    z = input('Qual operação deseja fazer? ( + , - , * , / ):')

    if (z == '+' or z == '-' or z == '*' or z == '/'):
        x = int(input('Digite o primeiro número:'))
        y = int(input('Digite o segundo número:'))

    if (z == '+'):
        total = x + y
        print ('{} + {} é igual a {}'.format(x, y, total))
        continue
    elif(z == '-'):
         total = x - y
         print('{} - {} é igual a {}'.format(x, y, total))
         continue
    elif(z == '*'):
        total= x * y
        print('{} * {} é igual a {}'.format(x, y, total))
        continue
    elif(z == '/'):
        total = x / y
        print('{} / {} é igual a {}'.format(x, y, total))
        continue
    elif(z == 's'):
        break
    else:
        print ('Operção inválida')

print('Encerrando programa.')
