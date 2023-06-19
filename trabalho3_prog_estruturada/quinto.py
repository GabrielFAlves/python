def calcular_total_faltas(lista):
    total_faltas = 0
    faltas_por_time = {}

    for jogo in lista:
        time1, time2 = jogo[0]
        faltas = jogo[1]

        total_faltas += faltas[0] + faltas[1]

        if time1 in faltas_por_time:
            faltas_por_time[time1] += faltas[0]
        else:
            faltas_por_time[time1] = faltas[0]

        if time2 in faltas_por_time:
            faltas_por_time[time2] += faltas[1]
        else:
            faltas_por_time[time2] = faltas[1]

    return total_faltas, faltas_por_time

# Lista de jogos
jogos = [
    [['Brasil', 'Italia'], [10, 9]],
    [['Brasil', 'Espanha'], [5, 7]],
    [['Italia', 'Espanha'], [7, 8]]
]

total_faltas, faltas_por_time = calcular_total_faltas(jogos)

time_menos_faltas = min(faltas_por_time, key=faltas_por_time.get)
if 'Brasil' in faltas_por_time and 'Espanha' in faltas_por_time:
    if faltas_por_time['Brasil'] == faltas_por_time['Espanha']:
        time_menos_faltas = 'Brasil, Espanha'

print("Total de faltas do campeonato:", total_faltas)
print("Time que fez mais faltas:", max(faltas_por_time, key=faltas_por_time.get))
print("Time que fez menos faltas:", time_menos_faltas)
