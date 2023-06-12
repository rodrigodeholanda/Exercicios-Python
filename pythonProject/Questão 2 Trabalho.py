print('Bem vindo a lanchonete do Rodrigo de Holanda - RU: 4335595')
print('*'*15,'Cardápio','*'*15)
print('|  Código  |       Descrição       |   Valor  |')
print('|   100    |    Cachorro Quente    |    9,00  |')
print('|   101    | Cachorro Quente Duplo |   11,00  |')
print('|   102    |         X-Egg         |   12,00  |')
print('|   103    |       X-Salada        |   13,00  |')
print('|   104    |        X-Bacon        |   14,00  |')
print('|   105    |        X-Tudo         |   17,00  |')
print('|   200    |   Refrigerante Lata   |    5,00  |')
print('|   201    |       Chá Gelado      |    5,00  |')

total = 0 #Recebe o valor total da somatória dos itens escolhidos
valor = 0 #Recebe o valor do item escolhido

while True:
    codigo = input("Digite o código do produto desejado:") #Recebe o codigo do produto
    #Condicionais para verificação dos intervalos dos codigos. O uso de 'and' foi feito para que, caso codigo receba algum valor diferente dos especificados, será exibido opção inválida.
    if (codigo != '100') and (codigo != '101') and (codigo != '102') and (codigo != '103') and (codigo != '104') and (codigo != '105') and (codigo != '200') and (codigo != '201'):
        print('opção inválida')
        continue #Continue foi inserido para retornar ao inicio do while
    #Caso algum dos valores acima seja true, o programa segue para o teste de condicionais para enquandrar o codigo ao item.
    elif(codigo == '100'):
        valor = 9 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um Cachorro Quente no valor de: R$9.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço

    elif(codigo == '101'):
        valor = 11 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um Cachorro Quente Duplo no valor de: R$11.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço

    elif(codigo == '102'):
        valor = 12 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um X-Egg no valor de: R$12.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço

    elif(codigo == '103'):
        valor = 13 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um X-Salada no valor de: R$13.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço

    elif(codigo == '104'):
        valor = 14 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um X-Bacon no valor de: R$14.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço

    elif(codigo == '105'):
        valor = 17 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um X-Tudo no valor de: R$17.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço

    elif(codigo == '200'):
        valor = 5 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um Refrigerante Lata no valor de: R$5.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço

    elif(codigo == '201'):
        valor = 5 #Valor do item escolhido
        total += valor #equação para calculo do valor total
        print('Você escolheu um Chá Gelado no valor de: R$5.00')
        print('Você deseja pedir algo a mais?')
        valida = input('1 - SIM\n0 - NÃO\n') #Comando para validar a continuidade ou não do pedido
        if valida == '1':
            continue #Continue foi inserido para retornar ao inicio do while
        elif valida == '0':
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço
        else:
            print('Valor digitado é inválido')
            print('Encerrando sua conta...')
            break #break foi inserido para encerrar o laço


    total += valor #equação para calculo do valor total



print('O valor total do pedido é R${:.2f}'.format(total))