import random

# Preenchendo o cubo com valores aleatórios
cubo = [[[random.randint(0, 100) for _ in range(50)] for _ in range(50)] for _ in range(50)]

# Inicialização das variáveis
soma_valores = 0
ocorrencias_90 = 0
maior_valor = 0
posicoes_maior_valor = []

# Percorrendo o cubo
for x in range(50):
    for y in range(50):
        for z in range(50):
            valor = cubo[x][y][z]
            soma_valores += valor
            if valor == 90:
                ocorrencias_90 += 1
            if valor > maior_valor:
                maior_valor = valor
                posicoes_maior_valor = [(x, y, z)]
            elif valor == maior_valor:
                posicoes_maior_valor.append((x, y, z))

# Exibindo os resultados
print("Soma dos valores no cubo:", soma_valores)
print("Número de ocorrências do valor 90:", ocorrencias_90)
print("Maior valor armazenado no cubo:", maior_valor)
print("Posições onde aparecem o maior valor:")
for posicao in posicoes_maior_valor:
    print(posicao)
