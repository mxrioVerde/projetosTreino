#1. Dada uma sequência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados. 
sequencia = input('Digite um número, ou 0 para encerrar o programa.')
sq = ''
if sequencia != 0 and sequencia != '':
    while sequencia != '0':
        digito = int(sequencia)
        sq += str(digito**2) + ','
        sequencia = input('Digite outro número, ou 0 para encerrar o programa.')
print(sq)
