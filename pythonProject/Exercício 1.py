print('Insira 3 valores relativos aos lados para saber qual o tipo de triângulo.')

x = int(input('Insira o Valor do primeiro lado:'))
y = int(input('Insira o Valor do segundo lado:'))
z = int(input('Insira o Valor do terceiro lado:'))

if (x>0 and y>0 and z>0):
    if (x < y + z and y < x + z and z < x + y):
        if (x == y and y == z):
            print('É um triângulo Equilátero.')
        else:
            if (x == y or y == z or x == z):
                print('É um triângulo Isórceles.')
            else:
                if (x != y and y != z):
                    print('É um triângulo Escaleno.')
    else:
        print('Um lado não pode ser maior que a soma dos outros dois.')
else:
    print('Os valores precisam ser acima de 0.')
