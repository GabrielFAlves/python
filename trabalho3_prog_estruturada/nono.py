import random

# Preenchendo o vetor com números aleatórios entre 0 e 20
vetor = [random.randint(0, 20) for _ in range(10)]

# Imprimindo o vetor original
print("Vetor original:", vetor)

# Manipulando os valores do vetor
for i in range(0, 10):
    vetor[i] += sum(vetor[:i])

# Imprimindo o vetor manipulado
print("Vetor manipulado:", vetor)
