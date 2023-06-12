print('Bem vindo(a) a Companhia de Logística Rodrigo de Holanda S.A - RU: 4335595')

def dimensoesObjeto(): #Primeira função criada para calcular as dimensões do objeto de acordo com os dados inseridos.

    while True:
        try: #Evitar erro caso o usuário digite valor não numérico
            a = float(input('Digite a altura do objeto (em cm):')) #Recebe o valor em cm da altura em numero real
            l = float(input('Digite a largura do objeto (em cm):')) #Recebe o valor em cm da largura em numero real
            d = float(input('Digite o diametro do objeto (em cm):')) #Recebe o valor em cm do diâmetro em numero real
            volume = a*l*d #Equação para calculo do volume
            print('O volume do objeto é de: {} cm³\n'.format(volume))
            #Condicionais para verificação dos intervalos de valores do volume
            if (volume < 1000):
                valorVolume = 10 #Valor assumido pela variavel 'valorVolume' caso a condicional seja verdadeira
                return valorVolume #retorno do valor em caso de true
            elif(volume >= 1000) and (volume < 10000): #Fiz o uso de 'and' para estreitarmos as possibilidades, sendo validado 'true' apenas se as duas condicionais (peso>=1) e (peso<10) forem verdadeiras.
                valorVolume = 20
                return valorVolume #retorno do valor em caso de true
            elif (volume >= 10000) and (volume < 30000):
                valorVolume = 30
                return valorVolume #retorno do valor em caso de true
            elif (volume >= 30000) and (volume < 100000):
                valorVolume = 50
                return valorVolume #retorno do valor em caso de true
            elif (volume >= 100000):
                print('Não aceitamos volumes tão grandes!\nEntre com as dimensões desejadas novamente.')
                continue #Volta para o inicio do While
        except ValueError:
            print('\nVocê digitou alguma dimensão com valor não numérico.\nDigite apenas valores numéricos.\n')
            continue #Volta para o inicio do While

def pesoObjeto():#Segunda função criada para definir o multiplicador do frete baseado no peso do objeto, de acordo com os intervalos dos valores.

    while True:
        try:#Evitar erro caso o usuário digite valor não numerico
            peso = float(input('Digite o peso do objeto (em kg):')) #Recebe o valor do peso do objeto em numero real
            # Condicionais para verificação dos intervalos de valores do peso
            if (peso < 0.1):
                multiplicadorPeso = 1
                return multiplicadorPeso #retorno do valor em caso de true
            elif(peso >= 0.1) and (peso < 1): #Fiz o uso de 'and' para estreitarmos as possibilidades, sendo validado 'true' apenas se as duas condicionais (peso>=1) e (peso<10) forem verdadeiras.
                multiplicadorPeso = 1.5
                return multiplicadorPeso #retorno do valor em caso de true
            elif (peso >= 1) and (peso < 10):
                multiplicadorPeso = 2
                return multiplicadorPeso #retorno do valor em caso de true
            elif (peso >= 10) and (peso < 30):
                multiplicadorPeso = 3
                return multiplicadorPeso #retorno do valor em caso de true
            elif (peso >=30):
                print('Não aceitamos objetos tão pesados!\nEntre com o peso desejado novamente.\n')
                continue #Volta para o inicio do While
        except ValueError:
            print('\nVocê digitou o peso com um valor não numérico.\nDigite apenas valores numéricos.\n')
            continue #Volta para o inicio do While

def rotaObjeto():#Terceira função criada para definir o multiplicador do frete baseado na rota definida de acordo com o escolhido.

    while True:
            print('Selecione a rota digitando a sigla:')
            print('FB - De Fortaleza para Bahia')
            print('FP - De Fortaleza para Pernambuco')
            print('FPB - De Fortaleza para Paraíba')
            print('FRN - De Fortaleza para Rio Grande do Norte')
            rota = (input('')).upper() #Recebe o o 'valor' da rota digitada em formato string
            #Teste da string recebida, validando de acordo com as condicionais abaixo:
            if (rota == 'fb') or (rota == 'Fb') or (rota == 'FB') or (rota == 'fB'): #Fiz uso de 'or' para que, caso pelo menos 1 dos valores de rota forem verdadeiros, a condicional é true.
                multiplicadorRota = 1
                return multiplicadorRota #retorno do valor em caso de true
            elif(rota == 'fp') or (rota == 'Fp') or (rota == 'FP') or (rota == 'fP'):
                multiplicadorRota = 1.2
                return multiplicadorRota #retorno do valor em caso de true
            elif (rota == 'fpb') or (rota == 'Fpb') or (rota == 'fPb') or (rota == 'fpB') or (rota == 'FPb') or (rota == 'fPB') or (rota == 'FpB') or (rota == 'FPB'):
                multiplicadorRota = 1.3
                return multiplicadorRota #retorno do valor em caso de true
            elif (rota == 'frn') or (rota == 'Frn') or (rota == 'fRn') or (rota == 'frN') or (rota == 'FRn') or (rota == 'fRN') or (rota == 'FrN') or (rota == 'FRN'):
                multiplicadorRota = 1.5
                return multiplicadorRota #retorno do valor em caso de true
            elif rota:
                print('Você digitou uma rota que não existe!\nEscolha novamente a rota desejada.\n')
                continue #Volta para o inicio do While

#Após a definição das funções, criei variáveis para montar a equação que resultaria no valor final do frete do objeto.

x = dimensoesObjeto() #Variável que assume a função 'dimensoesObjeto'
y = pesoObjeto() #Variável que assume a função 'pesoObjeto'
z = rotaObjeto() #Variável que assume a função 'rotaObjeto'
valortotal = x*y*z #Variável que assume a equação para calculo do valor total do frete, levando em consideração: volume*peso*rota.

print('O valor do frete pelo volume é de:R$ {}'.format(x))
print('O valor do multiplicador do peso é de: {}x'.format(y))
print('O valor do multiplicador da rota é de: {}x'.format(z))
print('O total a pagar (R$): {:.2f} (dimensões: {} * peso: {} * rota: {})'.format(valortotal, x, y, z))
