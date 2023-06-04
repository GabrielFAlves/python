# funçao para saber se digitou entre 0 e 5 inclusive
def obter_clube_preferencia():
    print("Clubes de futebol:")
    print("1 - Flamengo")
    print("2 - Vasco")
    print("3 - Fluminense")
    print("4 - Botafogo")
    print("5 - Outros")

    while True:
        clube = int(input("Digite o número correspondente ao clube de preferência (ou 0 para encerrar): "))
        if clube >= 0 and clube <= 5:
            return clube
        else:
            print("Opção inválida!")

# funçao para saber se o slário é >=0
def obter_salario():
    while True:
        salario = float(input("Digite o salário: "))
        if salario >= 0:
            return salario
        else:
            print("Salário inválido!")

# função para saber a cidade natal
def obter_cidade_natal():
    print("Cidades:")
    print("1 - Niterói")
    print("2 - Outra")

    while True:
        cidade = int(input("Digite o número correspondente à cidade natal: "))
        if cidade == 1 or cidade == 2:
            return cidade
        else:
            print("Opção inválida!")

# dicionários
# Inicialização das variáveis
torcedores_por_clube = {
    1: 0,  # Flamengo
    2: 0,  # Vasco
    3: 0,  # Fluminense
    4: 0,  # Botafogo
    5: 0   # Outros
}
salario_por_clube = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}
nascidos_em_niteroi_sem_clube = 0
total_entrevistados = 0

# Coleta dos dados
while True:
    clube_preferencia = obter_clube_preferencia()
    if clube_preferencia == 0:
        break

    salario = obter_salario()
    cidade_natal = obter_cidade_natal()

    torcedores_por_clube[clube_preferencia] += 1
    salario_por_clube[clube_preferencia].append(salario)
    total_entrevistados += 1

    if cidade_natal == 1 and clube_preferencia not in [1, 2, 3, 4]:
        nascidos_em_niteroi_sem_clube += 1

# clube é a chave / salarios é o valor
# Cálculo das médias salariais
medias_salariais = {}
for clube, salarios in salario_por_clube.items():
    if len(salarios) > 0:
        media = sum(salarios) / len(salarios)
        medias_salariais[clube] = media
    else:
        medias_salariais[clube] = 0

# Exibição dos resultados
print("Número de torcedores por clube:")
for clube, contagem in torcedores_por_clube.items():
    print("Clube", clube, ": ", contagem)

print("\nMédia salarial dos torcedores de cada clube:")
for clube, media in medias_salariais.items():
    print("Clube", clube, ": ", media)

print("\nNúmero de pessoas nascidas em Niterói e que não torcem para nenhum dos principais clubes do Rio: ", nascidos_em_niteroi_sem_clube)
print("Número de pessoas entrevistadas: ", total_entrevistados)
