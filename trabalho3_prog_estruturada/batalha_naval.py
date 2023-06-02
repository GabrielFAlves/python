import os

# criação do tabuleiro
while True:
    tabuleiro1 = []
    tabuleiro2 = []
    tabuleiro_vazio1 = []
    tabuleiro_vazio2 = []

    # área do submarinos
    for tabuleiro_cod in range(5):
        tabuleiro1.append(["o"] * 5)
        tabuleiro2.append(["o"] * 5)
        tabuleiro_vazio1.append(["o"] * 5)
        tabuleiro_vazio2.append(["o"] * 5)

    # coluna lateral de números
    numeros = list(range(1, 6))
    numeros = [str(num) for num in numeros]

    for coluna in range(len(numeros)):
        tabuleiro1[coluna].insert(0, numeros[coluna])

    for coluna in range(len(numeros)):
        tabuleiro2[coluna].insert(0, numeros[coluna])

    for coluna in range(len(numeros)):
        tabuleiro_vazio1[coluna].insert(0, numeros[coluna])

    for coluna in range(len(numeros)):
        tabuleiro_vazio2[coluna].insert(0, numeros[coluna])

    # usado para criar a separação entre as áreas do tabuleiro
    def mostra_tabuleiro(tabuleiro):
        for linha in tabuleiro:
            print(" ".join(linha))

# informação de onde vai estar os submarinos
    def submarino_posicionar(tabuleiro):
        submarino_numero = 1
        while submarino_numero < 4:
            print(f"Defina a posição do submarino número {submarino_numero}")
            linha = int(input(f"Informe a linha do submarino {submarino_numero}:")) - 1
            coluna = int(input(f"Informe a coluna do submarino {submarino_numero}:"))

            if linha < 0 or linha > len(tabuleiro) or coluna < 0 or coluna > len(tabuleiro):
                print("Posição inválida. Tente novamente")

            elif tabuleiro[linha][coluna] != "Sub":
                tabuleiro[linha][coluna] = "Sub"
                submarino_numero += 1

            else:
                print("Já existe um submarino nessa posição. Tente novamente")

# tentativa de acerto dos submarinos
    def tentativa_acerto(tabuleiro):
        while True:
            print("Tente acertar o submarino inimigo")
            linha = int(input("Escolha uma linha:")) - 1
            coluna = int(input("Escolha uma coluna:"))

            if linha < 0 or linha > len(tabuleiro) or coluna < 0 or coluna > len(tabuleiro):
                print("Esta posição não existe no mapa. Atire novamente.")

            else:
                return(linha, coluna)

# verificação dos tiros dados
    def verificar_palpite(palpite, tabuleiro, tabuleiro_vazio):
        linha, coluna = palpite

        if tabuleiro[linha][coluna] == "Sub":
            print("Aniquilação! Você acertou um submarino!")
            tabuleiro_vazio[linha][coluna] = "S"
            return True

        elif tabuleiro_vazio[linha][coluna] == "S" or tabuleiro_vazio[linha][coluna] == "X":
            print("Este local já foi atacado. Vamos adiante e de outro tiro!")
            return False

        else:
            print("Ainda temos inimigos. Você errou os submarinos.")
            tabuleiro_vazio[linha][coluna] = "X"
            return False

# usado para limpar o terminal após o ENTER
    def limpar_jogo():
        if os.name == "nt":
            os.system("cls")

        else:
            os.system("clear")

    j1 = input("Coloque o nome do primeiro jogador:")
    print("""
             1 2 3 4 5
           1 o o o o o
           2 o o o o o
           3 o o o o o
           4 o o o o o
           5 o o o o o
             """)
    submarino_posicionar(tabuleiro1)
    input("Aperter ENTER para que o segundo jogador possa jogar")
    limpar_jogo()

    print("--------------------------------------")

    j2 = input("Coloque o nome do segundo jogador:")
    print("""
             1 2 3 4 5
           1 o o o o o
           2 o o o o o
           3 o o o o o
           4 o o o o o
           5 o o o o o
             """)
    submarino_posicionar(tabuleiro2)
    input("Começar jogo")
    limpar_jogo()

    jogando = 1
    acertos1 = 0
    acertos2 = 0
    tiros1 = 0
    tiros2 = 0

# criação do jogador 1, junto aos dados anteriores para formar suas jogadas
    while acertos1 < 3 and acertos2 < 3:
        if jogando == 1:
            print(j1,",Pressione ENTER para que possa jogar")
            input()
            limpar_jogo()

            print("Jogador 1:", j1)
            print("Tiros dados:", tiros1,  "Acertos:", acertos1)
            print("  1 2 3 4 5")
            mostra_tabuleiro(tabuleiro_vazio1)
            palpite = tentativa_acerto(tabuleiro2)

            while tabuleiro_vazio1[palpite[0]][palpite[1]] in ["S", "X"]:
                print("Você já atirou nessa posição. Escolha um novo local.")
                palpite = tentativa_acerto(tabuleiro2)
            if verificar_palpite(palpite, tabuleiro2, tabuleiro_vazio1):
                acertos1 += 1
                if acertos1 == 3:
                    print(j1, "venceu a batalha! Mas a guerra nunca termina!")
                    break

            tiros1 += 1
            jogando = 2

# criação do jogador 2, junto aos dados anteriores para formar suas jogadas
        else:
            print(j2,",Pressione ENTER para que possa jogar")
            input()
            limpar_jogo()

            print("Jogador 2:", j2)
            print("Tiros dados:", tiros2, "Acertos:", acertos2)
            print("  1 2 3 4 5")
            mostra_tabuleiro(tabuleiro_vazio2)
            palpite = tentativa_acerto(tabuleiro1)

            while tabuleiro_vazio2[palpite[0]][palpite[1]] in ["S", "X"]:
                print("Você já atirou nessa posição. Escolha um novo local.")
                palpite = tentativa_acerto(tabuleiro1)
            if verificar_palpite(palpite, tabuleiro1, tabuleiro_vazio2):
                acertos2 += 1
                if acertos2 == 3:
                    print(j2, "venceu a batalha! Mas a guerra nunca termina!")
                    break

            tiros2 += 1
            jogando = 1

# reinicio do jogo
    reiniciar_jogo = input("Lutar novamente? (s/n)")
    limpar_jogo()

    if reiniciar_jogo.lower() != "s":
        break