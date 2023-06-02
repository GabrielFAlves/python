# a. Lista com os signos
signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

# b. Lista com as datas de aniversário dos membros da família
datas_aniversario = [1990, 1985, 2002, 1998]  # Exemplo de datas de aniversário

# c. Mostrar o signo de cada membro da família
# d. signo chines começou em 1900
# e. os signos estao na ordem errada
for ano in datas_aniversario:
    signo_index = (ano - 1900) % 12
    signo = signos[signo_index]
    print("Ano de nascimento:", ano, "- Signo:", signo)