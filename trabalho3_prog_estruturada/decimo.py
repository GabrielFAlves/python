# Tabela de preços dos produtos
tabela_precos = {
    'A': 3.50,
    'B': 4.00,
    'C': 5.50,
    'D': 7.50,
    'E': 9.00
}

# Variáveis para armazenar os dados das vendas
vendas = {
    'A': {'quantidade': 0, 'total_pago': 0},
    'B': {'quantidade': 0, 'total_pago': 0},
    'C': {'quantidade': 0, 'total_pago': 0},
    'D': {'quantidade': 0, 'total_pago': 0},
    'E': {'quantidade': 0, 'total_pago': 0}
}
total_arrecadado = 0
total_compras = 0

def exibir_menu():
    print("Menu de Preços:")
    for codigo, preco in tabela_precos.items():
        produto = obter_nome_produto(codigo)
        print(codigo + " - " + produto + ": R$" + str(preco))

def obter_nome_produto(codigo):
    if codigo == 'A':
        return "Refrigerante"
    elif codigo == 'B':
        return "Casquinha Simples"
    elif codigo == 'C':
        return "Casquinha Dupla"
    elif codigo == 'D':
        return "Sundae"
    elif codigo == 'E':
        return "Banana Split"

def processar_venda():
    venda = {}
    while True:
        codigo = input("Digite o código do produto (ou 0 para encerrar a venda): ")
        if codigo == '0':
            break
        quantidade = int(input("Digite a quantidade: "))
        if codigo in tabela_precos:
            preco_unitario = tabela_precos[codigo]
            valor_total = preco_unitario * quantidade
            venda[codigo] = {'quantidade': quantidade, 'valor_total': valor_total}
        else:
            print("Código de produto inválido!")

    return venda

def emitir_relatorio():
    print("Relatório de Vendas do Dia:")
    for codigo, dados_venda in vendas.items():
        produto = obter_nome_produto(codigo)
        quantidade = dados_venda['quantidade']
        total_pago = dados_venda['total_pago']
        print(produto + ":")
        print("  Quantidade vendida:", quantidade)
        print("  Total pago: R$", total_pago)
        print()

    print("Total arrecadado no dia: R$", total_arrecadado)
    if total_compras > 0:
        valor_medio = total_arrecadado / total_compras
        print("Valor médio por compra: R$", valor_medio)
    else:
        print("Nenhuma venda realizada.")

# Loop principal do programa
while True:
    exibir_menu()
    venda = processar_venda()
    if len(venda) == 0:
        break

    total_compras += 1
    for codigo, dados_item in venda.items():
        quantidade = dados_item['quantidade']
        valor_total = dados_item['valor_total']
        vendas[codigo]['quantidade'] += quantidade
        vendas[codigo]['total_pago'] += valor_total
        total_arrecadado += valor_total

    print("Venda registrada com sucesso!")

emitir_relatorio()
