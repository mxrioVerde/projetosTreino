#3. Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares. 
n = int(input('Digite um número.'))
sq = []
for i in range(n):
    sq.append(2*i + 1)
print(sq)