# Função para ler um vetor
def ler_vetor():
    vetor = []
    for i in range(10):
        elemento = float(input(f"Digite o valor do elemento {i+1}: "))
        vetor.append(elemento)
    return vetor

# Função para multiplicar os elementos dos vetores e criar o vetor resultante
def multiplicar_vetores(vetor1, vetor2):
    vetor_resultante = []
    for i in range(10):
        resultado = vetor1[i] * vetor2[i]
        vetor_resultante.append(resultado)
    return vetor_resultante

# Leitura dos dois vetores
print("Digite os elementos do primeiro vetor:")
vetor1 = ler_vetor()

print("\nDigite os elementos do segundo vetor:")
vetor2 = ler_vetor()

# Multiplicação dos vetores
vetor_resultante = multiplicar_vetores(vetor1, vetor2)

# Exibição do vetor resultante
print("\nVetor resultante:")
print(vetor_resultante)
