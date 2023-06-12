print('Bem vindo a Loja do Rodrigo de Holanda - Ru 4335595')

valor = float(input('Digite o valor do produto: R$'))
quantidade = int(input('Digite quantas unidades do produto você deseja:'))
total = valor*quantidade
#Teste condicional da variável 'Quantidade'

if (quantidade > 0) and (quantidade <= 9) and (valor > 0):
    x=1
    totaldesconto = total * x
    print('O valor sem desconto foi de: R${:.2f}'.format(total))
    print('O valor com desconto foi de: R${:.2f}  (0 % de desconto)'.format(totaldesconto))

elif (quantidade >= 10) and (quantidade <= 99) and (valor > 0):
    x = 5/100
    desconto = total * x
    totaldesconto = total - desconto
    print('O valor sem desconto foi de: R${:.2f}'.format(total))
    print('O valor com desconto foi de: R${:.2f}  (5 % de desconto)'.format(totaldesconto))
elif (quantidade >= 100) and (quantidade <= 999) and (valor > 0):
    x = 10/100
    desconto = total * x
    totaldesconto = total - desconto
    print('O valor sem desconto foi de: R${:.2f}'.format(total))
    print('O valor com desconto foi de: R${:.2f}  (10 % de desconto)'.format(totaldesconto))
elif (quantidade >= 1000) and (valor > 0):
    x = 15/100
    desconto = total * x
    totaldesconto = total - desconto
    print('O valor sem desconto foi de: R${:.2f}'.format(total))
    print('O valor com desconto foi de: R${:.2f}  (15 % de desconto)'.format(totaldesconto))
else:
    print("Um dos valores inseridos não é valido !")

# Dentro do 'if', preferi usar 'and' para condicionar os valores aceitos, pois achei mais organizado e consegui definir
# melhor os intervalos os quais pretendia trabalhar dentro do objetivo da questão. Em relação ao 'elif', preferi usa-lo
# na situação de termos um valor diferente dos abordados, pois existia a chance do usuário digitar uma quantidade ou
# um preço que fossem iguais a '0'. Acredito que dessa forma os intervalos foram expressos de uma melhor forma.