#2. Dado um número inteiro positivo n, calcular a soma dos n primeiros números inteiros positivos. 
n = int(input('Digite um número.'))
total = 0
for i in range(1, n+1):
    total += i
print(total)