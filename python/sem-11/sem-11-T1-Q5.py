def calcular_ano_mes(salario, divida):
    
    ano = 2016
    mes = 10 
    aumento_anual = 0.05
    juros_mensal = 0.15 
    mes_aumento_salario = 3 
    divida_atual = divida
    
    while divida_atual <= salario:

        mes += 1
        if mes > 12:
            mes = 1
            ano += 1
        divida_atual *= (1 + juros_mensal)
        
        if mes == mes_aumento_salario:
            salario *= (1 + aumento_anual)
    
    return mes, ano

def main():
    salario = float(input("Digite o valor do salário: R$ "))
    divida = float(input("Digite o valor da dívida: R$ "))
    mes, ano = calcular_ano_mes(salario, divida)
    print(f"{mes}/{ano}")

if __name__ == "__main__":
    main()
