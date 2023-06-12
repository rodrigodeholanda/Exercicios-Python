print('Insira os valores para que seja feita a operação algébrica desejada')
x = int(input('Insira o primeiro valor:'))
y = int(input('Insira o segundo valor:'))
a = float
print('+ - Adição')
print('- - Subtração')
print('* - Multiplicação')
print('/ - Divisão')

z = input('Qual operação você deseja realizar?')

if (z == '+'):
    a = x + y
    print('O resultado de {} + {} = {}.'.format(x,y,a))

elif (z == '-'):
    a = x - y
    print('O resultado de {} - {} = {}.'.format(x,y,a))

elif (z == '*'):
    a = x * y
    print('O resultado de {} * {} = {}.'.format(x,y,a))

elif (z == '/'):
    a = x / y
    print('O resultado de {} / {} = {}.'.format(x,y,a))

else:
    print("Insira um valor válido !")
