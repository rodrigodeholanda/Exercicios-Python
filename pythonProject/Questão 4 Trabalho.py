#'Bem vindo ao controle de estoque da bicicletaria do Rodrigo de Holanda - RU: 4335595'

#Variáveis Globais
listaPeca = []
codigoPeca = 0


#Funções:
def cadastrar_peca(codigo):#Função criada para cadastrar produtos
    print('Codigo da Peça:{}'.format(codigo))
    nomePeca = input('Por favor entre com o NOME da Peça:')
    fabricantePeca = input('Por favor entre com o FABRICANTE da peça:')
    valorPeca = input('Por favor entre com o VALOR (R$) da peça:')
    dicionarioPeca ={'Código da Peça'    : codigo,
                     'Nome da Peça'      : nomePeca,
                     'Fabricante da Peça': fabricantePeca,
                     'Valor da Peça'     : valorPeca}
    listaPeca.append(dicionarioPeca.copy())

def consultar_peca():# Função criada para consultar produtos
    while True:

        print('\nMENU CONSULTA DE PEÇAS:')
        print('1 - Consultar Todas as Peças.')
        print('2 - Consultar Peças por Código.')
        print('3 - Consultar Peças por Fabricante.')
        print('4 - Retornar.')
        opcao_menu2 = input('Escolha a opção desejada no menu de consulta:\n>>')

        if (opcao_menu2 == '1'):
            print('Consultar Todas as Peças.\n')
            for peca in listaPeca: #Peca vai varrer a lista de peças
                print('-' *25)
                for chave, valor in peca.items(): #varredura da chave e do valor de cada dicionario peça
                    print('{} : {:2}'.format(chave, valor))

        elif (opcao_menu2 == '2'):
            print('Consultar Peças por Código.\n')
            valordesejado = int((input('Digite o código da peça desejada:\n>>')))
            for peca in listaPeca:
                if peca['Código da Peça'] == valordesejado: #Comparação do codigo inserido com o que há armazenado no dicionario.
                    print('-' * 25)
                    for chave, valor in peca.items():  # varredura da chave e do valor de cada dicionario peça
                        print('{} : {:2}'.format(chave, valor))

        elif (opcao_menu2 == '3'):
            print('Consultar Peças por Fabricante.\n')
            valordesejado = input('Digite o nome do Fabricante:\n>>')
            for peca in listaPeca:
                if peca['Fabricante da Peça'] == valordesejado:  # Comparação do codigo inserido com o que há armazenado no dicionario.
                    print('-' * 25)
                    for chave, valor in peca.items():  # varredura da chave e do valor de cada dicionario peça
                        print('{} : {:2}'.format(chave, valor))


        elif (opcao_menu2 == '4'):
            print('Retornar ao Menu Principal.\n')
            return #Sai da função consultar peças e retorna ao menu principal
        else:
            print('Opção Inválida. Tente novamente.')
            continue  # Volta ao inicio do laço while


def remover_peca(): # Função criada para remover produtos
    valordesejado = int(input('Digite o CÓDIGO da peça que deseja remover:\n>>'))
    for peca in listaPeca:
        if peca['Código da Peça'] == valordesejado:  # Comparação do codigo inserido com o que há armazenado no dicionario.
            listaPeca.remove(peca)
            print('Produto Removido.')

#Inicio do programa :

print('Bem vindo ao controle de estoque da bicicletaria do Rodrigo de Holanda - RU: 4335595')

while True:

    print ('\nMENU DO ESTOQUE:')
    print('1 - Cadastrar Peças.')
    print('2 - Consultar Peças.')
    print('3 - Remover Peças.')
    print('4 - Sair.')
    opcao_menu1 = input('Escolha a opção desejada no menu:\n>>')

    if (opcao_menu1 == '1'):
        print('Você selecionou a opção cadastrar peças.\n')
        codigoPeca += 1
        cadastrar_peca(codigoPeca)

    elif(opcao_menu1 == '2'):
        print('Você selecionou a opção consultar peças.\n')
        consultar_peca()

    elif (opcao_menu1 == '3'):
        print('Você selecionou a opção remover peças.\n')
        remover_peca()

    elif(opcao_menu1 == '4'):
        print('Encerrando programa...')
        break #Encerra o laço principal
    else:
        print('Opção Inválida. Tente novamente.')
        continue #Volta ao inicio do laço while