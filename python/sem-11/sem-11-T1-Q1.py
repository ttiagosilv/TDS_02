def calcular_anos_para_dobrar(deposito_inicial, taxa_juros):

    valor_atual = deposito_inicial
    anos = 0
    valor_desejado = 2 * deposito_inicial
    
    while valor_atual < valor_desejado:
        valor_atual += valor_atual * (taxa_juros / 100)
        anos += 1
    return anos

def main():
    depoimento_inicial = float(input("Digite o valor do depósito inicial (em R$): "))
    taxa_juros = float(input("Digite a taxa de juros anual (em %): "))

    anos_necessarios = calcular_anos_para_dobrar(depoimento_inicial, taxa_juros)
    print(f"O valor acumulado será o dobro do valor inicial em {anos_necessarios} anos.")

if __name__ == "__main__":
    main()
