contador_masculino = 0  # Variável para contar o número de pessoas do sexo masculino
contador_feminino_18_25 = 0  # Variável para contar o número de mulheres na faixa etária de 18 a 25 anos
soma_idades = 0  # Variável para somar as idades
quantidade_pessoas = 0  # Variável para contar o número total de pessoas

while True:
    idade = int(input("Digite a idade (digite 0 para sair): "))
    
    if idade == 0:
        break  # Encerra o loop se a idade for igual a zero
    
    sexo = int(input("Digite o sexo (0 - masculino, 1 - feminino): "))
    
    soma_idades += idade
    quantidade_pessoas += 1
    
    if sexo == 0:
        contador_masculino += 1
    elif sexo == 1 and 18 <= idade <= 25:
        contador_feminino_18_25 += 1

if quantidade_pessoas > 0:
    media_idades = soma_idades / quantidade_pessoas
else:
    media_idades = 0

print("Idade média:", media_idades)
print("Mulheres na faixa etária de 18 a 25 anos:", contador_feminino_18_25)
print("Número total de homens:", contador_masculino)
