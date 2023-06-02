while True:
    numero = int(input("Digite um número inteiro positivo (0 para sair): "))
    if numero == 0:
        break
    
    divisor = []
    
    # Encontrar divisores positivos diferentes de n
    for i in range(1, numero):
        if numero % i == 0:
            divisor.append(i)
    
    # Verificar se a soma dos divisores é igual ao número
    if sum(divisor) == numero:
        print(numero, "é um número perfeito!")
    else:
        print(numero, "não é um número perfeito.")
    
    print()
