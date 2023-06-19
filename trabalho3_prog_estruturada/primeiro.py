def ano_bissexto(ano):
    """Verifica se um ano é bissexto."""
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def dia_mes(ano, mes):
    """Retorna o número de dias em um determinado mês."""
    if mes == 2:
        return 29 if ano_bissexto(ano) else 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def diferenca_data(data_inicio, data_fim):
    """Calcula o número de dias entre duas datas."""
    ano_inicio, mes_inicio, dia_inicio = data_inicio
    ano_fim, mes_fim, dia_fim = data_fim

    dias = 0

    while data_inicio != data_fim:
        dias += 1
        dia_inicio += 1

        if dia_inicio > dia_mes(ano_inicio, mes_inicio):
            dia_inicio = 1
            mes_inicio += 1

            if mes_inicio > 12:
                mes_inicio = 1
                ano_inicio += 1

        data_inicio = (ano_inicio, mes_inicio, dia_inicio)

    return dias

# Função principal
ano_inicio = int(input("Digite o ano da primeira data (4 dígitos): "))
mes_inicio = int(input("Digite o mês da primeira data: "))
dia_inicio = int(input("Digite o dia da primeira data: "))

ano_fim = int(input("Digite o ano da segunda data (4 dígitos): "))
mes_fim = int(input("Digite o mês da segunda data: "))
dia_fim = int(input("Digite o dia da segunda data: "))

data_inicio = (ano_inicio, mes_inicio, dia_inicio)
data_fim = (ano_fim, mes_fim, dia_fim)

dias = diferenca_data(data_inicio, data_fim)
print("Número de dias corridos:", dias)
