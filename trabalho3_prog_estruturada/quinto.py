# Lista de jogos e faltas
lista_jogos = [
    [['Brasil', 'Italia', [10, 9]]],
    [['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7, 8]]]
]

# Dicionário para armazenar as faltas por time
faltas_por_time = {}

# Percorrer a lista de jogos e faltas
for jogos in lista_jogos:
    for jogo in jogos:
        time1 = jogo[0]
        time2 = jogo[1]
        faltas_time1, faltas_time2 = jogo[2]

        # Atualizar o dicionário de faltas por time
        if time1 in faltas_por_time:
            faltas_por_time[time1] += faltas_time1
        else:
            faltas_por_time[time1] = faltas_time1

        if time2 in faltas_por_time:
            faltas_por_time[time2] += faltas_time2
        else:
            faltas_por_time[time2] = faltas_time2

# Encontrar o total de faltas do campeonato
total_faltas = sum(faltas_por_time.values())

# Encontrar o time com mais faltas
time_com_mais_faltas = max(faltas_por_time, key=faltas_por_time.get)

# Encontrar o time com menos faltas
time_com_menos_faltas = min(faltas_por_time, key=faltas_por_time.get)

# Exibir resultados
print("Total de faltas do campeonato:", total_faltas)
print("Time com mais faltas:", time_com_mais_faltas)
print("Time com menos faltas:", time_com_menos_faltas)
