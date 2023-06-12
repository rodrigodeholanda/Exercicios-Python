#Elaboração função para cálculo de fatorial com a confirmação de q x é inteiro:
def valida_int(pergunta, min,max):
    x = int(input(pergunta))
    while ((x<min) or (x>max)):
        x = int(input(pergunta))
    return x
def fatorial(num):
    """
    Calcula a fatorial
    """
    fat = 1
    if (num == 0):
        return fat
    for i in range (1, num+1,1):
        fat*=i
    return fat
#Programa Principal:
x = valida_int('Digite o valor para calcular a fatorial:',0,999999)
print ('{}!={}'.format(x, fatorial(x)))
