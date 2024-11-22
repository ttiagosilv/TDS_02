def calcular_meses_para_comprar_carro(preco_carro_atual):
    poupanca = 10000.0 
    taxa_poupanca = 0.007
    taxa_inflacao_carro = 0.004
    meses = 0

    while poupanca < preco_carro_atual:
        preco_carro_atual *= (1 + taxa_inflacao_carro)
        poupanca *= (1 + taxa_poupanca)
        meses += 1

    return meses

preco_carro_atual = float(input("Digite o preço do carro hoje: "))
meses = calcular_meses_para_comprar_carro(preco_carro_atual)
print(f"Você terá dinheiro suficiente para comprar o carro em {meses} meses.")
