#Ingresso Cinema


x = input('Digite sua idade para saber o preço do seu ingresso:')
ingresso = int
total =0
dinheiro = 0
while True:
    if (x == 'sair'):
      break

    x = int(x)
    total = total + 1

    if (x<3):
        ingresso = 0
        print('Seu ingresso é gratuito.')
    else:
        if (x>12):
            ingresso = 30
            print('Seu ingresso custa R$30.')
        else:
            ingresso = 15
            print('Seu ingressso custa R$15.')

    dinheiro = dinheiro + ingresso

    x = input('Digite sua idade para saber o preço do seu ingresso:')

media = dinheiro / total

print('Total de pessoas:{}'.format(total))
print('Total arrecadado:{}'.format(dinheiro))
print('média arrecadada:{}'.format(media))
