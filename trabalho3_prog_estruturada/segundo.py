# função para saber se é palindromo
def palindromo(numero):
    digitos = list(str(numero))
    inverte_digitos = digitos[::-1]
    return digitos == inverte_digitos

num = input("Digite um número inteiro de 5 dígitos: ")

# loop para saber se o numero é inteiro de 5 digitos
while not (num.isdigit() and len(num) == 5):
    print("Entrada inválida. Digite um número inteiro de 5 dígitos válido.")
    num = input("Digite um número inteiro de 5 dígitos: ")

numero = int(num)

if palindromo(numero):
    print("O número é um palíndromo!")
else:
    print("O número não é um palíndromo.")