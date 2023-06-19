numeros = []  # Lista vazia para armazenar os números

# Loop para receber os três números do usuário
for i in range(3):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)  # Adiciona o número à lista

numeros.sort()  # Ordena a lista em ordem crescente

print("Os números em ordem crescente são:")
for numero in numeros:
    print(numero)