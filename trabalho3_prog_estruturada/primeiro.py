def is_leap_year(year):
    """Verifica se um ano é bissexto."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Retorna o número de dias em um determinado mês."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def date_difference(start_date, end_date):
    """Calcula o número de dias entre duas datas."""
    start_year, start_month, start_day = start_date
    end_year, end_month, end_day = end_date

    days = 0

    while start_date != end_date:
        days += 1
        start_day += 1

        if start_day > days_in_month(start_year, start_month):
            start_day = 1
            start_month += 1

            if start_month > 12:
                start_month = 1
                start_year += 1

        start_date = (start_year, start_month, start_day)

    return days

# Função principal
def main():
    while True:
        start_year = int(input("Digite o ano da primeira data (4 dígitos): "))
        if start_year == 0:
            break

        start_month = int(input("Digite o mês da primeira data: "))
        start_day = int(input("Digite o dia da primeira data: "))

        end_year = int(input("Digite o ano da segunda data (4 dígitos): "))
        end_month = int(input("Digite o mês da segunda data: "))
        end_day = int(input("Digite o dia da segunda data: "))

        start_date = (start_year, start_month, start_day)
        end_date = (end_year, end_month, end_day)

        days = date_difference(start_date, end_date)
        print("Número de dias corridos:", days)
        print()

if __name__ == "__main__":
    main()
