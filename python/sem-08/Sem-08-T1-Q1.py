from datetime import datetime

def calcular_idade(data_nascimento, data_atual):
    anos = data_atual.year - data_nascimento.year
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        anos -= 1
    return anos

def main():
  
    # Obtendo a data atual
    dia_atual = int(input("Digite o dia atual: "))
    mes_atual = int(input("Digite o mês atual: "))
    ano_atual = int(input("Digite o ano atual: "))
    
      # Obtendo a data de nascimento do usuário
    dia_nascimento = int(input("Digite o dia de nascimento: "))
    mes_nascimento = int(input("Digite o mês de nascimento: "))
    ano_nascimento = int(input("Digite o ano de nascimento: "))

    data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
    data_atual = datetime(ano_atual, mes_atual, dia_atual)

    # Calculando a idade
    idade = calcular_idade(data_nascimento, data_atual)

    # Exibindo a idade
    print("A idade é:", idade, "anos")

if __name__ == "__main__":
    main()