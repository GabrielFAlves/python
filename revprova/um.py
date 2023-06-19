n = int(input("Digite o valor de n: "))  # Solicita o valor de n ao usuário
soma_quadrados = 0  # Variável para armazenar a soma dos quadrados

for i in range(n):
    valor = float(input(f"Digite o valor {i+1}: "))  # Solicita cada valor ao usuário
    soma_quadrados += valor ** 2  # Calcula o quadrado do valor e adiciona à soma

print("A soma dos quadrados dos valores é:", soma_quadrados)  # Exibe a soma dos quadrados
