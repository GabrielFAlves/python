import random

# Preencher o vetor com números aleatórios entre 0 e 20
vetor = [random.randint(0, 20) for _ in range(10)]

print("Vetor original:", vetor)

# Realizar o shift para a direita
vetor_manipulado = [vetor[-1]] + vetor[:-1]

print("Vetor manipulado:", vetor_manipulado)
