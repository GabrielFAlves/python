# Função para calcular o somatório de uma coluna da matriz
def calcular_somatorio_coluna(matriz, coluna):
    somatorio = 0
    for i in range(len(matriz)):
        somatorio += matriz[i][coluna]
    return somatorio

# Função para calcular o produto de uma linha da matriz
def calcular_produto_linha(matriz, linha):
    produto = 1
    for j in range(len(matriz[linha])):
        produto *= matriz[linha][j]
    return produto

# Matriz A de tamanho 4x5
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

# Cálculo do somatório dos elementos da quarta coluna
coluna_quatro = 3
somatorio_coluna_quatro = calcular_somatorio_coluna(A, coluna_quatro)

# Cálculo do produto dos elementos da terceira linha
linha_tres = 2
produto_linha_tres = calcular_produto_linha(A, linha_tres)

# Exibição dos resultados
print("Somatório dos elementos da quarta coluna:", somatorio_coluna_quatro)
print("Produto dos elementos da terceira linha:", produto_linha_tres)
