def calcular_prestacoes(valor_compra):
    for parcelas in range(1, 25):
        prestacao = valor_compra / parcelas
        print(f"{parcelas}x de R$ {prestacao:.2f}")

def main():
    valor_compra = float(input(""))
    calcular_prestacoes(valor_compra)

if __name__ == "__main__":
    main()
