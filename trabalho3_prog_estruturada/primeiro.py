# função para saber se é ano bixesto
def eh_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def dias_entre_datas(data_inicial, data_final):
    dia_inicial, mes_inicial, ano_inicial = data_inicial
    dia_final, mes_final, ano_final = data_final

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ano_inicial == ano_final:
        dias = sum(dias_por_mes[mes_inicial - 1:mes_final - 1])
        if eh_ano_bissexto(ano_inicial) and mes_inicial <= 2 <= mes_final:
            dias += 1
    else:
        dias = sum(dias_por_mes[mes_inicial - 1:])
        if eh_ano_bissexto(ano_inicial) and mes_inicial <= 2:
            dias += 1

        for ano in range(ano_inicial + 1, ano_final):
            if eh_ano_bissexto(ano):
                dias += 366
            else:
                dias += 365

        if eh_ano_bissexto(ano_final) and mes_final >= 3:
            dias += 1
        dias += sum(dias_por_mes[:mes_final - 1])

    return dias


def obter_data():
    data_str = input("Digite a data (dd/mm/aaaa): ")
    dia, mes, ano = map(int, data_str.split('/'))
    return dia, mes, ano


# Programa principal
while True:
    data_inicial = obter_data()
    if data_inicial == (0, 0, 0):
        break

    data_final = obter_data()
    if data_final == (0, 0, 0):
        break

    dias = dias_entre_datas(data_inicial, data_final)
    print("Número de dias corridos:", dias)
