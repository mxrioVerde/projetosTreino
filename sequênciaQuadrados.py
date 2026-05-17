sequencia = input('Digite um número, ou 0 para encerrar o programa.')
sq = ''
if sequencia != 0:
    while sequencia != '0':
        digito = int(sequencia)
        sq += str(digito**2) + ','
        sequencia = input('Digite outro número, ou 0 para encerrar o programa.')
print(sq)